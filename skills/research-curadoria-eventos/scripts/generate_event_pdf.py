#!/usr/bin/env python3
"""Generate a polished PDF agenda from curated event JSON.

The input can be either an array of event objects or an object containing
`eventos`/`events` plus optional metadata. Event objects should include the
skill's required fields and may include:

- imagem_url: direct image URL from the event source
- imagem_fonte: URL of the page where the image was found
- fonte_nome: human-readable source name
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import mimetypes
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)


class ImageFinder(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.meta_images: list[str] = []
        self.body_images: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {k.lower(): (v or "") for k, v in attrs}
        if tag.lower() == "meta":
            key = (values.get("property") or values.get("name") or "").lower()
            if key in {"og:image", "og:image:url", "twitter:image", "twitter:image:src"}:
                content = values.get("content", "").strip()
                if content:
                    self.meta_images.append(content)
        elif tag.lower() == "img":
            src = values.get("src", "").strip()
            if not src or src.startswith("data:"):
                return
            label = " ".join(values.get(k, "") for k in ("alt", "class", "id", "src")).lower()
            if any(skip in label for skip in ("logo", "icon", "avatar", "captcha")):
                return
            self.body_images.append(src)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to JSON input file")
    parser.add_argument("--output", required=True, help="Path to PDF output file")
    parser.add_argument("--title", default="", help="Report title")
    parser.add_argument("--subtitle", default="", help="Report subtitle")
    parser.add_argument(
        "--html-only",
        action="store_true",
        help="Only write the HTML companion file; useful when no PDF renderer is available",
    )
    parser.add_argument(
        "--no-fetch-images",
        action="store_true",
        help="Do not try to discover images from each event link",
    )
    parser.add_argument(
        "--allow-missing-images",
        action="store_true",
        help="Generate the PDF even when one or more events have no source image",
    )
    return parser.parse_args()


def read_payload(path: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if isinstance(payload, list):
        return {}, [dict(item) for item in payload]
    if isinstance(payload, dict):
        raw_events = payload.get("eventos", payload.get("events", []))
        if not isinstance(raw_events, list):
            raise ValueError("The JSON object must contain an 'eventos' array.")
        return payload, [dict(item) for item in raw_events]
    raise ValueError("Input JSON must be an array or an object with an 'eventos' array.")


def text(value: Any) -> str:
    return "" if value is None else str(value).strip()


def esc(value: Any) -> str:
    return html.escape(text(value), quote=True)


def fetch_bytes(url: str, timeout: int = 20) -> tuple[bytes, str]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        content_type = response.headers.get("content-type", "").split(";")[0].strip()
        return response.read(), content_type


def decode_html(data: bytes) -> str:
    sample = data[:2000].decode("ascii", errors="ignore")
    match = re.search(r"charset=[\"']?([a-zA-Z0-9._-]+)", sample, re.I)
    encoding = match.group(1) if match else "utf-8"
    return data.decode(encoding, errors="replace")


def absolutize(url: str, base_url: str) -> str:
    if not url:
        return ""
    return urllib.parse.urljoin(base_url, url)


def find_source_image(source_url: str) -> str:
    if not source_url.startswith(("http://", "https://")):
        return ""
    try:
        data, content_type = fetch_bytes(source_url)
    except Exception:
        return ""
    if "html" not in content_type and content_type:
        return ""
    parser = ImageFinder()
    try:
        parser.feed(decode_html(data))
    except Exception:
        return ""
    candidates = parser.meta_images or parser.body_images
    return absolutize(candidates[0], source_url) if candidates else ""


def image_as_data_uri(image_url: str) -> str:
    if not image_url:
        return ""
    if image_url.startswith("data:image/"):
        return image_url
    try:
        if image_url.startswith(("http://", "https://")):
            data, content_type = fetch_bytes(image_url)
        else:
            path = Path(image_url)
            data = path.read_bytes()
            content_type = mimetypes.guess_type(path.name)[0] or "image/jpeg"
    except Exception:
        return ""
    if not content_type:
        content_type = mimetypes.guess_type(image_url)[0] or "image/jpeg"
    if not content_type.startswith("image/"):
        return ""
    encoded = base64.b64encode(data).decode("ascii")
    return f"data:{content_type};base64,{encoded}"


def category_class(category: str) -> str:
    normalized = category.lower()
    if any(term in normalized for term in ("musica", "show", "samba", "concerto")):
        return "music"
    if any(term in normalized for term in ("gastronomia", "festival", "feira")):
        return "food"
    if any(term in normalized for term in ("teatro", "circo", "danca", "infantil")):
        return "stage"
    if any(term in normalized for term in ("esporte", "automobil")):
        return "sport"
    return "default"


def source_host(url: str) -> str:
    try:
        host = urllib.parse.urlparse(url).netloc
    except Exception:
        return ""
    return host.replace("www.", "")


def prepare_events(
    events: list[dict[str, Any]],
    fetch_images: bool,
    require_images: bool,
) -> list[dict[str, Any]]:
    prepared: list[dict[str, Any]] = []
    missing_images: list[str] = []
    for event in events:
        item = {k: text(v) for k, v in event.items()}
        source_url = item.get("imagem_fonte") or item.get("fonte_url") or item.get("link_venda")
        image_url = item.get("imagem_url") or item.get("image_url")
        if fetch_images and not image_url and source_url:
            image_url = find_source_image(source_url)
            if image_url:
                item["imagem_url"] = image_url
                item["imagem_fonte"] = source_url
        item["imagem_data_uri"] = image_as_data_uri(image_url)
        if require_images and not item["imagem_data_uri"]:
            missing_images.append(item.get("evento") or f"evento {len(prepared) + 1}")
        item["source_host"] = source_host(source_url)
        prepared.append(item)
    if missing_images:
        names = "; ".join(missing_images[:8])
        extra = "" if len(missing_images) <= 8 else f"; +{len(missing_images) - 8} outros"
        raise SystemExit(
            "Missing source images for these events: "
            f"{names}{extra}. Add imagem_url from the event source or rerun with --allow-missing-images."
        )
    return prepared


def build_html(
    metadata: dict[str, Any],
    events: list[dict[str, Any]],
    title: str,
    subtitle: str,
) -> str:
    report_title = title or text(metadata.get("titulo")) or text(metadata.get("title")) or "Agenda de eventos"
    report_subtitle = (
        subtitle
        or text(metadata.get("subtitulo"))
        or text(metadata.get("subtitle"))
        or text(metadata.get("periodo"))
    )
    generated_at = datetime.now().strftime("%d/%m/%Y %H:%M")
    total = len(events)
    cards = "\n".join(build_event_card(event, index + 1) for index, event in enumerate(events))
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <title>{esc(report_title)}</title>
  <style>
    @page {{ size: A4; margin: 16mm 14mm; }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: #1c2430;
      font-family: Arial, Helvetica, sans-serif;
      background: #f6f7f9;
      line-height: 1.45;
    }}
    .cover {{
      color: #ffffff;
      background: linear-gradient(135deg, #0f6f73 0%, #143642 58%, #c44d34 100%);
      border-radius: 22px;
      padding: 30px;
      margin-bottom: 18px;
      min-height: 210px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: 0 18px 38px rgba(20, 54, 66, 0.18);
    }}
    .eyebrow {{
      text-transform: uppercase;
      letter-spacing: 0.12em;
      font-size: 11px;
      font-weight: 700;
      opacity: 0.82;
    }}
    h1 {{
      margin: 18px 0 8px;
      font-size: 34px;
      line-height: 1.08;
      letter-spacing: 0;
    }}
    .subtitle {{
      max-width: 620px;
      margin: 0;
      font-size: 15px;
      color: rgba(255, 255, 255, 0.86);
    }}
    .cover-footer {{
      display: flex;
      justify-content: space-between;
      gap: 16px;
      font-size: 12px;
      color: rgba(255, 255, 255, 0.82);
    }}
    .event-card {{
      background: #ffffff;
      border: 1px solid #dde4e8;
      border-radius: 18px;
      overflow: hidden;
      margin: 0 0 14px;
      page-break-inside: avoid;
      box-shadow: 0 10px 28px rgba(15, 28, 36, 0.08);
    }}
    .event-image {{
      width: 100%;
      height: 205px;
      object-fit: cover;
      display: block;
      background: #dfe7ea;
    }}
    .image-missing {{
      height: 140px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: repeating-linear-gradient(135deg, #e7edf0, #e7edf0 10px, #d8e1e5 10px, #d8e1e5 20px);
      color: #52636b;
      font-size: 13px;
      font-weight: 700;
    }}
    .event-body {{ padding: 18px 20px 20px; }}
    .event-top {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 14px;
      margin-bottom: 10px;
    }}
    h2 {{
      margin: 0;
      font-size: 21px;
      line-height: 1.18;
      letter-spacing: 0;
      color: #14252f;
    }}
    .number {{
      flex: 0 0 auto;
      width: 34px;
      height: 34px;
      border-radius: 50%;
      background: #143642;
      color: #ffffff;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 13px;
      font-weight: 700;
    }}
    .meta {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px 16px;
      margin: 14px 0;
      font-size: 12.5px;
    }}
    .meta strong {{
      display: block;
      color: #66747c;
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 2px;
    }}
    .summary {{
      margin: 10px 0 14px;
      color: #34444d;
      font-size: 13.5px;
    }}
    .chip {{
      display: inline-block;
      border-radius: 999px;
      padding: 6px 10px;
      font-size: 11px;
      font-weight: 700;
      color: #ffffff;
      background: #5865a8;
    }}
    .chip.music {{ background: #0f6f73; }}
    .chip.food {{ background: #c44d34; }}
    .chip.stage {{ background: #7c4d8b; }}
    .chip.sport {{ background: #2d6f3f; }}
    .footer-row {{
      border-top: 1px solid #edf1f3;
      margin-top: 14px;
      padding-top: 12px;
      display: flex;
      justify-content: space-between;
      gap: 14px;
      font-size: 11.5px;
      color: #5a6b73;
    }}
    a {{ color: #0f6f73; text-decoration: none; font-weight: 700; }}
    .source {{ max-width: 55%; }}
  </style>
</head>
<body>
  <section class="cover">
    <div>
      <div class="eyebrow">Curadoria de eventos</div>
      <h1>{esc(report_title)}</h1>
      <p class="subtitle">{esc(report_subtitle)}</p>
    </div>
    <div class="cover-footer">
      <span>{total} evento(s) curado(s)</span>
      <span>Gerado em {esc(generated_at)}</span>
    </div>
  </section>
  {cards}
</body>
</html>
"""


def build_event_card(event: dict[str, Any], index: int) -> str:
    category = event.get("categoria", "")
    chip_class = category_class(category)
    source_url = event.get("imagem_fonte") or event.get("fonte_url") or event.get("link_venda")
    source_name = event.get("fonte_nome") or event.get("source_host") or "Fonte"
    link = event.get("link_venda", "")
    image = event.get("imagem_data_uri", "")
    image_html = (
        f'<img class="event-image" src="{image}" alt="{esc(event.get("evento"))}">'
        if image
        else '<div class="image-missing">Imagem indisponivel na fonte</div>'
    )
    source_link = (
        f'<a href="{esc(source_url)}">{esc(source_name)}</a>' if source_url else esc(source_name)
    )
    event_link = f'<a href="{esc(link)}">Abrir link</a>' if link else "Link nao informado"
    return f"""
  <article class="event-card">
    {image_html}
    <div class="event-body">
      <div class="event-top">
        <div>
          <span class="chip {chip_class}">{esc(category or "Evento")}</span>
          <h2>{esc(event.get("evento"))}</h2>
        </div>
        <span class="number">{index}</span>
      </div>
      <div class="meta">
        <div><strong>Data e horario</strong>{esc(event.get("data_hora"))}</div>
        <div><strong>Preco</strong>{esc(event.get("preco"))}</div>
        <div><strong>Local</strong>{esc(event.get("local"))}</div>
        <div><strong>Categoria</strong>{esc(category)}</div>
      </div>
      <p class="summary">{esc(event.get("resumo"))}</p>
      <div class="footer-row">
        <span class="source">Imagem/fonte: {source_link}</span>
        <span>{event_link}</span>
      </div>
    </div>
  </article>
"""


def render_with_playwright(html_path: Path, output_path: Path) -> bool:
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except Exception:
        return False
    try:
        with sync_playwright() as runner:
            browser = None
            for kwargs in ({}, {"channel": "msedge"}, {"channel": "chrome"}):
                try:
                    browser = runner.chromium.launch(headless=True, **kwargs)
                    break
                except Exception:
                    pass
            if browser is None:
                return False
            page = browser.new_page()
            page.goto(html_path.as_uri(), wait_until="networkidle")
            page.pdf(
                path=str(output_path),
                format="A4",
                print_background=True,
                prefer_css_page_size=True,
            )
            browser.close()
            return output_path.exists() and output_path.stat().st_size > 0
    except Exception:
        return False


def render_with_weasyprint(html_path: Path, output_path: Path) -> bool:
    try:
        from weasyprint import HTML  # type: ignore
    except Exception:
        return False
    try:
        HTML(filename=str(html_path)).write_pdf(str(output_path))
        return output_path.exists() and output_path.stat().st_size > 0
    except Exception:
        return False


def browser_candidates() -> list[str]:
    names = ["msedge", "chrome", "chromium"]
    candidates = [shutil.which(name) for name in names]
    if os.name == "nt":
        candidates.extend(
            [
                r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
                r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            ]
        )
    return [str(Path(c)) for c in candidates if c and Path(c).exists()]


def render_with_browser(html_path: Path, output_path: Path) -> bool:
    for browser in browser_candidates():
        with tempfile.TemporaryDirectory() as tmpdir:
            command = [
                browser,
                "--headless=new",
                "--disable-gpu",
                "--no-sandbox",
                f"--user-data-dir={tmpdir}",
                f"--print-to-pdf={output_path}",
                html_path.as_uri(),
            ]
            try:
                subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except Exception:
                continue
            if output_path.exists() and output_path.stat().st_size > 0:
                return True
    return False


def render_pdf(html_content: str, output_path: Path, html_only: bool) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    html_path = output_path.with_suffix(".html")
    html_path.write_text(html_content, encoding="utf-8")
    if html_only:
        return html_path
    renderers = (render_with_playwright, render_with_weasyprint, render_with_browser)
    for renderer in renderers:
        if renderer(html_path, output_path):
            return output_path
    raise SystemExit(
        "Could not render PDF. HTML was generated at "
        f"{html_path}. Install Playwright/WeasyPrint or use a Chromium-based browser."
    )


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).resolve()
    output_path = Path(args.output).resolve()
    metadata, events = read_payload(input_path)
    prepared_events = prepare_events(
        events,
        fetch_images=not args.no_fetch_images,
        require_images=not args.allow_missing_images,
    )
    html_content = build_html(metadata, prepared_events, args.title, args.subtitle)
    created = render_pdf(html_content, output_path, args.html_only)
    print(created)
    return 0


if __name__ == "__main__":
    sys.exit(main())
