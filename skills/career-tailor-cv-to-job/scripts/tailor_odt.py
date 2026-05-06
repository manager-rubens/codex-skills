#!/usr/bin/env python3
"""Apply audited replacements to an ODT while preserving the package structure."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET


TEXT_NS = "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}"

RUBEN_REQUIRED_TERMS = [
    "Claude Code",
    "OpenAi Codex",
    "Agent Skills",
    "Claude Code in Action - Anthropic",
    "Introduction to Agent Skills - Anthropic",
    "Introduction to Model Context Protocol - Anthropic",
    "Buiding with the Claude API - Anthropic",
]


@dataclass(frozen=True)
class Replacement:
    old: str
    new: str
    expected: int = 1
    note: str = ""


@dataclass(frozen=True)
class TextSegment:
    tag: str
    style: str
    text: str


@dataclass(frozen=True)
class VisibleParagraph:
    line_index: int
    text: str
    segments: list[TextSegment]


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def local_name(name: str) -> str:
    return name.rsplit("}", 1)[-1] if "}" in name else name


def element_style(elem: ET.Element) -> str:
    for key, value in elem.attrib.items():
        if local_name(key) == "style-name":
            return value
    return ""


def collect_text_segments(elem: ET.Element) -> list[TextSegment]:
    segments: list[TextSegment] = []

    def visit(node: ET.Element) -> None:
        if node.text:
            segments.append(TextSegment(local_name(node.tag), element_style(node), node.text))
        for child in list(node):
            visit(child)
            if child.tail:
                segments.append(TextSegment(local_name(node.tag), element_style(node), child.tail))

    visit(elem)
    return segments


def read_content(document: Path) -> str:
    with zipfile.ZipFile(document, "r") as archive:
        return archive.read("content.xml").decode("utf-8")


def visible_paragraphs(content: str) -> list[VisibleParagraph]:
    root = ET.fromstring(content.encode("utf-8"))
    paragraphs: list[VisibleParagraph] = []
    line_index = 0
    for elem in root.iter():
        if elem.tag in {TEXT_NS + "p", TEXT_NS + "h"}:
            text = clean_text("".join(elem.itertext()))
            if text:
                line_index += 1
                paragraphs.append(
                    VisibleParagraph(
                        line_index=line_index,
                        text=text,
                        segments=collect_text_segments(elem),
                    )
                )
    return paragraphs


def extract_text(content: str) -> list[str]:
    lines: list[str] = []
    for paragraph in visible_paragraphs(content):
        lines.append(paragraph.text)
    return lines


def dump_text(document: Path) -> None:
    content = read_content(document)
    for index, line in enumerate(extract_text(content), 1):
        print(f"{index:03}: {line}")


def find_visible_text_fragment(document: Path, fragment: str) -> int:
    normalized_fragment = clean_text(fragment)
    if not normalized_fragment:
        print("Fragment must contain visible text.", file=sys.stderr)
        return 2

    content = read_content(document)
    matches = [
        paragraph
        for paragraph in visible_paragraphs(content)
        if normalized_fragment in paragraph.text
    ]

    if not matches:
        print(f"No visible paragraph/header contains: {fragment!r}", file=sys.stderr)
        return 1

    for match_number, paragraph in enumerate(matches, 1):
        if match_number > 1:
            print()
        print(f"Match {match_number} (visible line {paragraph.line_index:03}):")
        print(f"Visible: {paragraph.text}")
        print("Text-node segments:")
        for segment_index, segment in enumerate(paragraph.segments, 1):
            if not segment.text:
                continue
            style = f" style={segment.style}" if segment.style else ""
            print(f"  {segment_index:02}: <{segment.tag}{style}> {segment.text!r}")
        print("Tip: use one or more exact segment texts above as smaller replacement keys.")

    return 0


def load_replacements(path: Path) -> list[Replacement]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Invalid replacement JSON at {path}:{exc.lineno}:{exc.colno}: {exc.msg}"
        ) from exc
    if isinstance(raw, dict):
        items = [{"old": old, "new": new} for old, new in raw.items()]
    elif isinstance(raw, list):
        items = raw
    else:
        raise ValueError("Replacement JSON must be an object or a list of objects.")

    replacements: list[Replacement] = []
    for item in items:
        if not isinstance(item, dict) or "old" not in item or "new" not in item:
            raise ValueError("Each replacement must include 'old' and 'new'.")
        replacements.append(
            Replacement(
                old=str(item["old"]),
                new=str(item["new"]),
                expected=int(item.get("expected", 1)),
                note=str(item.get("note", "")),
            )
        )
    return replacements


def replacement_to_dict(replacement: Replacement) -> dict[str, object]:
    item: dict[str, object] = {
        "old": replacement.old,
        "new": replacement.new,
        "expected": replacement.expected,
    }
    if replacement.note:
        item["note"] = replacement.note
    return item


def paragraph_matches(content: str, visible_text: str) -> list[VisibleParagraph]:
    normalized = clean_text(visible_text)
    return [
        paragraph
        for paragraph in visible_paragraphs(content)
        if paragraph.text == normalized
    ]


def split_label_body(text: str) -> tuple[str, str] | None:
    if ":" not in text:
        return None
    split_at = text.index(":") + 1
    if split_at < len(text) and text[split_at] == " ":
        split_at += 1
    return text[:split_at], text[split_at:]


def segment_texts(paragraph: VisibleParagraph) -> list[str]:
    return [segment.text for segment in paragraph.segments if segment.text]


def make_segment_replacements(
    content: str,
    replacement: Replacement,
) -> list[Replacement]:
    exact_count = content.count(replacement.old)
    if exact_count == replacement.expected:
        return [replacement]

    matches = paragraph_matches(content, replacement.old)
    if len(matches) != 1:
        raise ValueError(
            f"Expected one visible paragraph for {replacement.old!r}, found {len(matches)}."
        )

    paragraph = matches[0]
    texts = segment_texts(paragraph)
    if not texts:
        raise ValueError(f"Visible line {paragraph.line_index:03} has no replaceable text nodes.")
    note = f"auto-split from visible line {paragraph.line_index:03}"

    if len(texts) == 1:
        return [Replacement(old=texts[0], new=replacement.new, expected=1, note=note)]

    old_joined = "".join(texts)
    new_text = replacement.new

    leading_count = 0
    leading_length = 0
    for text in texts:
        if new_text.startswith(text, leading_length):
            leading_count += 1
            leading_length += len(text)
        else:
            break
    if leading_count and leading_count < len(texts):
        old_tail = texts[leading_count:]
        new_tail = new_text[leading_length:]
        if len(old_tail) == 1:
            return [
                Replacement(
                    old=old_tail[0],
                    new=new_tail,
                    expected=1,
                    note=f"{note}; preserved {leading_count} leading styled segment(s)",
                )
            ]
        combined_old_tail = "".join(old_tail)
        if content.count(combined_old_tail) == 1:
            return [
                Replacement(
                    old=combined_old_tail,
                    new=new_tail,
                    expected=1,
                    note=f"{note}; preserved {leading_count} leading styled segment(s)",
                )
            ]

    old_label_body = split_label_body(old_joined)
    new_label_body = split_label_body(new_text)
    if old_label_body and new_label_body and len(texts) == 2:
        new_label, new_body = new_label_body
        suggestions = [
            Replacement(old=texts[0], new=new_label, expected=1, note=f"{note}; label segment"),
            Replacement(old=texts[1], new=new_body, expected=1, note=f"{note}; body segment"),
        ]
        return [item for item in suggestions if item.old != item.new]

    raise ValueError(
        "Could not auto-split styled visible replacement. Use "
        "--find-visible-text-fragment and add smaller replacements manually: "
        f"{replacement.old!r}"
    )


def print_segment_hint(content: str, replacement: Replacement) -> None:
    matches = paragraph_matches(content, replacement.old)
    if len(matches) != 1:
        print(f"  Hint: no unique visible paragraph match for {replacement.old!r}")
        return
    paragraph = matches[0]
    print(f"  Hint: visible line {paragraph.line_index:03} has these text-node segments:")
    for index, segment in enumerate(paragraph.segments, 1):
        if not segment.text:
            continue
        style = f" style={segment.style}" if segment.style else ""
        print(f"    {index:02}: <{segment.tag}{style}> {segment.text!r}")


def validate_replacements(document: Path, replacements_path: Path) -> int:
    try:
        replacements = load_replacements(replacements_path)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 2

    content = read_content(document)
    ok = True
    seen_old: dict[str, int] = {}
    for index, replacement in enumerate(replacements, 1):
        if replacement.old in seen_old:
            ok = False
            print(
                f"FAIL {index:03}: duplicate old text also used by item "
                f"{seen_old[replacement.old]:03}: {replacement.old!r}"
            )
            continue
        seen_old[replacement.old] = index
        count = content.count(replacement.old)
        status = "OK" if count == replacement.expected else "FAIL"
        print(
            f"{status} {index:03}: expected={replacement.expected} found={count} "
            f"old={replacement.old!r}"
        )
        if count != replacement.expected:
            ok = False
            if count == 0:
                print_segment_hint(content, replacement)
    return 0 if ok else 1


def suggest_segment_replacements(
    document: Path,
    replacements_path: Path,
    output_path: Path,
) -> int:
    try:
        replacements = load_replacements(replacements_path)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 2

    content = read_content(document)
    suggested: list[Replacement] = []
    for replacement in replacements:
        try:
            suggested.extend(make_segment_replacements(content, replacement))
        except ValueError as exc:
            print(exc, file=sys.stderr)
            return 1

    seen_old: dict[str, int] = {}
    for index, replacement in enumerate(suggested, 1):
        if replacement.old in seen_old:
            print(
                f"Suggested replacement {index:03} duplicates old text from "
                f"item {seen_old[replacement.old]:03}: {replacement.old!r}",
                file=sys.stderr,
            )
            return 1
        seen_old[replacement.old] = index

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps([replacement_to_dict(item) for item in suggested], ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )
    print(output_path)
    print(f"wrote {len(suggested)} replacement item(s)")
    return 0


def apply_replacements(content: str, replacements: list[Replacement]) -> tuple[str, list[tuple[Replacement, int]]]:
    applied: list[tuple[Replacement, int]] = []
    for replacement in replacements:
        count = content.count(replacement.old)
        if count != replacement.expected:
            raise RuntimeError(
                "Expected {expected} occurrence(s), found {count}: {old!r}".format(
                    expected=replacement.expected,
                    count=count,
                    old=replacement.old,
                )
            )
        content = content.replace(replacement.old, replacement.new)
        applied.append((replacement, count))
    ET.fromstring(content.encode("utf-8"))
    return content, applied


def write_odt(source: Path, output: Path, content: str) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(source, "r") as zin, zipfile.ZipFile(output, "w") as zout:
        if "mimetype" in zin.namelist():
            info = zin.getinfo("mimetype")
            zi = zipfile.ZipInfo("mimetype", date_time=info.date_time)
            zi.external_attr = info.external_attr
            zi.compress_type = zipfile.ZIP_STORED
            zout.writestr(zi, zin.read("mimetype"))

        for info in zin.infolist():
            if info.filename == "mimetype":
                continue
            data = content.encode("utf-8") if info.filename == "content.xml" else zin.read(info.filename)
            zi = zipfile.ZipInfo(info.filename, date_time=info.date_time)
            zi.external_attr = info.external_attr
            zi.compress_type = info.compress_type
            zout.writestr(zi, data)


def write_audit(
    audit_path: Path,
    source: Path,
    output: Path,
    applied: list[tuple[Replacement, int]],
    required_terms: list[str],
    competencies: list[str],
    omitted: list[str],
) -> None:
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "ODT tailored with scripts/tailor_odt.py.",
        f"Source preserved: {source}",
        f"Output generated: {output}",
        "",
        f"Applied replacements: {len(applied)}",
    ]
    if competencies:
        lines.extend(["", "Competencies targeted:"] + [f"- {item}" for item in competencies])
    if omitted:
        lines.extend(["", "Omitted unsupported keywords:"] + [f"- {item}" for item in omitted])
    if required_terms:
        lines.extend(["", "Required terms verified:"] + [f"- {item}" for item in required_terms])
    lines.extend(["", "Replacement log:"])
    for replacement, count in applied:
        note = f" ({replacement.note})" if replacement.note else ""
        lines.append(f"- count={count}{note}: {replacement.old} -> {replacement.new}")
    audit_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Apply audited text/XML replacements to an ODT file.")
    parser.add_argument("source", help="Source ODT file. This file is never modified.")
    parser.add_argument("--output", required=False, help="Output ODT path.")
    parser.add_argument("--replacements", help="UTF-8 JSON object or list with old/new replacements.")
    parser.add_argument("--audit", help="Optional audit text file path.")
    parser.add_argument("--require-term", action="append", default=[], help="Visible text that must remain in the output.")
    parser.add_argument("--ruben-required", action="store_true", help="Verify Ruben's required AI/tool/course additions.")
    parser.add_argument("--competency", action="append", default=[], help="Competency targeted, written to the audit file.")
    parser.add_argument("--omitted", action="append", default=[], help="Unsupported vacancy keyword omitted, written to the audit file.")
    parser.add_argument("--dump-text", action="store_true", help="Print visible paragraphs/headings and exit without editing.")
    parser.add_argument(
        "--validate-replacements",
        metavar="JSON",
        help="Validate replacement JSON syntax and exact content.xml match counts without editing.",
    )
    parser.add_argument(
        "--suggest-segment-replacements",
        metavar="JSON",
        help="Convert visible-line replacements into smaller styled text-node replacements when possible.",
    )
    parser.add_argument(
        "--suggest-output",
        help="Output JSON path for --suggest-segment-replacements.",
    )
    parser.add_argument(
        "--find-visible-text-fragment",
        metavar="TEXT",
        help="Find visible paragraphs/headings containing TEXT and print their actual text-node/span segments.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    source = Path(args.source).expanduser().resolve()
    if not source.exists() or source.suffix.lower() != ".odt":
        print(f"Input ODT not found: {source}", file=sys.stderr)
        return 2

    if args.dump_text:
        dump_text(source)
        return 0

    if args.validate_replacements:
        return validate_replacements(
            source,
            Path(args.validate_replacements).expanduser().resolve(),
        )

    if args.suggest_segment_replacements:
        if not args.suggest_output:
            parser.error("--suggest-output is required with --suggest-segment-replacements")
        return suggest_segment_replacements(
            source,
            Path(args.suggest_segment_replacements).expanduser().resolve(),
            Path(args.suggest_output).expanduser().resolve(),
        )

    if args.find_visible_text_fragment:
        return find_visible_text_fragment(source, args.find_visible_text_fragment)

    if not args.output or not args.replacements:
        parser.error("--output and --replacements are required unless --dump-text or --find-visible-text-fragment is used.")

    output = Path(args.output).expanduser().resolve()
    try:
        replacements = load_replacements(Path(args.replacements).expanduser().resolve())
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 2
    required_terms = list(args.require_term)
    if args.ruben_required:
        required_terms.extend(term for term in RUBEN_REQUIRED_TERMS if term not in required_terms)

    content = read_content(source)

    content, applied = apply_replacements(content, replacements)
    visible_text = "\n".join(extract_text(content))
    missing_terms = [term for term in required_terms if term not in visible_text]
    if missing_terms:
        print("Required term(s) missing after replacement:", file=sys.stderr)
        for term in missing_terms:
            print(f"- {term}", file=sys.stderr)
        return 4

    write_odt(source, output, content)
    if args.audit:
        write_audit(
            Path(args.audit).expanduser().resolve(),
            source,
            output,
            applied,
            required_terms,
            list(args.competency),
            list(args.omitted),
        )

    print(output)
    print(f"applied {len(applied)} replacements")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
