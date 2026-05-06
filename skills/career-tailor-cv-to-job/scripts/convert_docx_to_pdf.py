#!/usr/bin/env python3
"""Convert an editable document file to PDF with LibreOffice/OpenOffice/soffice."""

from __future__ import annotations

import argparse
import contextlib
import os
import shutil
import socket
import subprocess
import sys
import tempfile
from pathlib import Path


UNO_EXPORT_SCRIPT = r'''
import os
import sys
import time

import uno
from com.sun.star.beans import PropertyValue


def prop(name, value):
    item = PropertyValue()
    item.Name = name
    item.Value = value
    return item


def file_url(path):
    return uno.systemPathToFileUrl(os.path.abspath(path))


def main():
    if len(sys.argv) != 4:
        sys.stderr.write("usage: uno_export.py input output port\n")
        return 2

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    port = sys.argv[3]

    local_ctx = uno.getComponentContext()
    resolver = local_ctx.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver",
        local_ctx,
    )

    ctx = None
    last_error = None
    for _ in range(80):
        try:
            ctx = resolver.resolve(
                "uno:socket,host=localhost,port=%s;urp;StarOffice.ComponentContext" % port
            )
            break
        except Exception as exc:
            last_error = exc
            time.sleep(0.25)
    if ctx is None:
        sys.stderr.write("Could not connect to UNO service: %s\n" % last_error)
        return 3

    smgr = ctx.ServiceManager
    desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
    doc = desktop.loadComponentFromURL(
        file_url(input_path),
        "_blank",
        0,
        (prop("Hidden", True), prop("ReadOnly", True)),
    )
    if doc is None:
        sys.stderr.write("Could not load document: %s\n" % input_path)
        return 4

    try:
        doc.storeToURL(
            file_url(output_path),
            (prop("FilterName", "writer_pdf_Export"), prop("Overwrite", True)),
        )
    finally:
        doc.close(True)

    print(os.path.abspath(output_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''


def find_soffice() -> str | None:
    found = shutil.which("soffice") or shutil.which("libreoffice")
    if found:
        return found

    candidates = [
        Path(r"C:\Program Files\LibreOffice\program\soffice.exe"),
        Path(r"C:\Program Files (x86)\LibreOffice\program\soffice.exe"),
        Path(r"C:\Program Files\OpenOffice 4\program\soffice.exe"),
        Path(r"C:\Program Files (x86)\OpenOffice 4\program\soffice.exe"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return None


def find_office_python(soffice: str) -> str:
    program_dir = Path(soffice).resolve().parent
    candidates = [
        program_dir / "python.exe",
        program_dir / "python",
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return sys.executable


def is_openoffice(soffice: str) -> bool:
    return "openoffice" in str(Path(soffice)).lower()


def user_installation_arg(profile_dir: Path | None) -> str | None:
    if profile_dir is None:
        return None
    return "-env:UserInstallation=file:///%s" % profile_dir.resolve().as_posix().lstrip("/")


def free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def safe_pdf_name(name: str) -> str:
    cleaned = "".join("_" if char in '<>:"/\\|?*' else char for char in name).strip()
    if not cleaned.lower().endswith(".pdf"):
        cleaned += ".pdf"
    return cleaned


def expected_pdf(document_path: Path, output_dir: Path) -> Path:
    return output_dir / f"{document_path.stem}.pdf"


def final_pdf_path(generated: Path, output_dir: Path, pdf_name: str | None) -> Path:
    if not pdf_name:
        return generated
    return output_dir / safe_pdf_name(pdf_name)


def remove_stale(path: Path) -> None:
    if path.exists():
        path.unlink()


def move_to_final(generated: Path, final_path: Path) -> Path:
    if generated.resolve() != final_path.resolve():
        if final_path.exists():
            final_path.unlink()
        generated.rename(final_path)
    return final_path


def print_process_output(result: subprocess.CompletedProcess[str]) -> None:
    if result.stdout:
        print(result.stdout, file=sys.stderr)
    if result.stderr:
        print(result.stderr, file=sys.stderr)


def kill_process_tree(process: subprocess.Popen[str]) -> None:
    if process.poll() is not None:
        return
    if os.name == "nt":
        subprocess.run(
            ["taskkill", "/PID", str(process.pid), "/T", "/F"],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=10,
        )
        return
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=5)


def run_command_with_timeout(
    command: list[str],
    timeout: int,
    env: dict[str, str] | None = None,
    startupinfo: subprocess.STARTUPINFO | None = None,
) -> subprocess.CompletedProcess[str]:
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=env,
        startupinfo=startupinfo,
    )
    try:
        stdout, stderr = process.communicate(timeout=timeout)
        return subprocess.CompletedProcess(command, process.returncode or 0, stdout, stderr)
    except subprocess.TimeoutExpired:
        kill_process_tree(process)
        return subprocess.CompletedProcess(
            command,
            124,
            "",
            "Command timed out after %ss: %s" % (timeout, " ".join(command)),
        )


def run_convert_to(
    soffice: str,
    document_path: Path,
    output_dir: Path,
    timeout: int,
    profile_dir: Path | None,
) -> subprocess.CompletedProcess[str]:
    command = [
        soffice,
        "--headless",
        "--convert-to",
        "pdf",
        "--outdir",
        str(output_dir),
        str(document_path),
    ]
    profile_arg = user_installation_arg(profile_dir)
    if profile_arg:
        command.insert(1, profile_arg)
    return run_command_with_timeout(command, timeout)


def run_uno_export(
    soffice: str,
    document_path: Path,
    generated: Path,
    timeout: int,
    profile_dir: Path | None,
) -> subprocess.CompletedProcess[str]:
    port = str(free_port())
    program_dir = Path(soffice).resolve().parent
    office_python = find_office_python(soffice)

    startupinfo = None
    if os.name == "nt":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    server_command = [
        soffice,
        "-headless",
        "-nofirststartwizard",
        "-accept=socket,host=localhost,port=%s;urp;StarOffice.ServiceManager" % port,
    ]
    profile_arg = user_installation_arg(profile_dir)
    if profile_arg:
        server_command.insert(1, profile_arg)

    server = subprocess.Popen(
        server_command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        startupinfo=startupinfo,
    )
    try:
        with tempfile.TemporaryDirectory(prefix="codex-uno-export-") as temp_dir:
            script_path = Path(temp_dir) / "uno_export.py"
            script_path.write_text(UNO_EXPORT_SCRIPT, encoding="utf-8")
            env = os.environ.copy()
            py_path = str(program_dir)
            if env.get("PYTHONPATH"):
                py_path = py_path + os.pathsep + env["PYTHONPATH"]
            env["PYTHONPATH"] = py_path
            return run_command_with_timeout(
                [office_python, str(script_path), str(document_path), str(generated), port],
                timeout=timeout,
                env=env,
            )
    finally:
        kill_process_tree(server)


def convert_document(
    soffice: str,
    document_path: Path,
    output_dir: Path,
    pdf_name: str | None,
    timeout: int,
    use_uno_fallback: bool,
    attempts: int,
    isolated_profile: bool,
    prefer_uno: bool,
) -> Path:
    generated = expected_pdf(document_path, output_dir)
    final_path = final_pdf_path(generated, output_dir, pdf_name)
    remove_stale(generated)
    if final_path != generated:
        remove_stale(final_path)

    methods = ["uno", "convert-to"] if prefer_uno and use_uno_fallback else ["convert-to"]
    if use_uno_fallback and "uno" not in methods:
        methods.append("uno")
    attempts = max(1, attempts)
    failures: list[str] = []

    for attempt in range(1, attempts + 1):
        profile_context = (
            tempfile.TemporaryDirectory(prefix="codex-office-profile-")
            if isolated_profile
            else contextlib.nullcontext(None)
        )
        with profile_context as profile_name:
            profile_dir = Path(profile_name) if profile_name else None
            profile_note = f" with isolated profile {profile_dir}" if profile_dir else ""
            for method in methods:
                remove_stale(generated)
                print(
                    f"PDF export attempt {attempt}/{attempts}: {method}{profile_note}.",
                    file=sys.stderr,
                )
                if method == "convert-to":
                    result = run_convert_to(soffice, document_path, output_dir, timeout, profile_dir)
                else:
                    result = run_uno_export(soffice, document_path, generated, timeout, profile_dir)

                if result.returncode == 0 and generated.exists():
                    return move_to_final(generated, final_path)

                reason = (result.stderr or result.stdout or "").strip()
                if not reason and result.returncode == 0:
                    reason = f"{method} returned success but did not create {generated}"
                elif not reason:
                    reason = f"{method} failed with exit code {result.returncode}"
                failures.append(f"attempt {attempt} {method}: {reason}")
                print_process_output(result)

    details = "\n".join(f"- {failure}" for failure in failures[-6:])
    raise RuntimeError(f"PDF export failed after {attempts} attempt(s). Recent failures:\n{details}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert DOCX/ODT/RTF to PDF using LibreOffice/OpenOffice.")
    parser.add_argument("document", help="Path to the editable document file to convert")
    parser.add_argument("--output-dir", default=None, help="Directory for the generated PDF")
    parser.add_argument("--pdf-name", default=None, help="Final PDF filename")
    parser.add_argument("--timeout", type=int, default=120, help="Timeout in seconds for each export stage. Default: 120.")
    parser.add_argument("--attempts", type=int, default=1, help="Number of full export attempts. Default: 1.")
    parser.add_argument("--no-uno-fallback", action="store_true", help="Disable the UNO fallback used when --convert-to fails silently.")
    parser.add_argument("--prefer-uno", action="store_true", help="Try the UNO exporter before --convert-to.")
    parser.add_argument("--prefer-convert-to", action="store_true", help="Try --convert-to before UNO even for OpenOffice.")
    parser.add_argument("--no-isolated-profile", action="store_true", help="Reuse the current Office profile instead of a temporary isolated profile.")
    args = parser.parse_args()

    document_path = Path(args.document).expanduser().resolve()
    if not document_path.exists():
        print(f"Input file not found: {document_path}", file=sys.stderr)
        return 2
    if document_path.suffix.lower() not in {".docx", ".odt", ".rtf"}:
        print("Input must be a .docx, .odt, or .rtf file.", file=sys.stderr)
        return 2

    output_dir = Path(args.output_dir).expanduser().resolve() if args.output_dir else document_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    soffice = find_soffice()
    if not soffice:
        print("LibreOffice/soffice was not found. Install LibreOffice or export the document to PDF manually.", file=sys.stderr)
        return 3

    try:
        prefer_uno = args.prefer_uno or (is_openoffice(soffice) and not args.prefer_convert_to)
        final_path = convert_document(
            soffice,
            document_path,
            output_dir,
            args.pdf_name,
            args.timeout,
            not args.no_uno_fallback,
            args.attempts,
            not args.no_isolated_profile,
            prefer_uno,
        )
    except Exception as exc:  # noqa: BLE001 - CLI should report actionable export failures.
        print(str(exc), file=sys.stderr)
        return 4

    print(final_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
