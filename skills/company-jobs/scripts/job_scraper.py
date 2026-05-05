#!/usr/bin/env python3
"""Best-effort company careers scraper for Codex skills.

The script intentionally uses only the Python standard library so it can run in
fresh Codex environments without dependency installation.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from typing import Any
from urllib.parse import urldefrag, urljoin, urlparse
from urllib.request import Request, urlopen


CAREER_TERMS = (
    "career",
    "careers",
    "job",
    "jobs",
    "opening",
    "openings",
    "position",
    "positions",
    "vacancy",
    "vacancies",
    "vagas",
    "trabalhe-conosco",
    "work-with-us",
    "join-us",
    "join-our-team",
)

ATS_HOSTS = (
    "boards.greenhouse.io",
    "job-boards.greenhouse.io",
    "jobs.lever.co",
    "jobs.ashbyhq.com",
    "myworkdayjobs.com",
    "jobs.smartrecruiters.com",
    "recruitee.com",
    "apply.workable.com",
    "bamboohr.com",
    "gupy.io",
    "jobs.kenoby.com",
    "teamtailor.com",
    "comeet.com",
)

GENERIC_LINK_TEXT = {
    "apply",
    "apply now",
    "view",
    "view job",
    "view role",
    "learn more",
    "read more",
    "see more",
    "all jobs",
    "open positions",
    "current openings",
    "vagas",
    "jobs",
}


@dataclass(frozen=True)
class Job:
    title: str
    url: str
    location: str = ""
    department: str = ""
    employment_type: str = ""
    source: str = ""


class CareersParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.links: list[tuple[str, str]] = []
        self.json_ld: list[str] = []
        self._tag_stack: list[str] = []
        self._current_link: dict[str, str] | None = None
        self._in_title = False
        self._in_json_ld = False
        self._buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {key.lower(): value or "" for key, value in attrs}
        self._tag_stack.append(tag)
        if tag == "title":
            self._in_title = True
            self._buffer = []
        elif tag == "script" and "ld+json" in attrs_dict.get("type", "").lower():
            self._in_json_ld = True
            self._buffer = []
        elif tag == "a" and attrs_dict.get("href"):
            self._current_link = {"href": attrs_dict["href"], "text": ""}

    def handle_endtag(self, tag: str) -> None:
        if tag == "title" and self._in_title:
            self.title = clean_text(" ".join(self._buffer))
            self._in_title = False
        elif tag == "script" and self._in_json_ld:
            self.json_ld.append("".join(self._buffer).strip())
            self._in_json_ld = False
        elif tag == "a" and self._current_link:
            text = clean_text(self._current_link["text"])
            if text:
                self.links.append((self._current_link["href"], text))
            self._current_link = None
        if self._tag_stack:
            self._tag_stack.pop()

    def handle_data(self, data: str) -> None:
        if self._in_title or self._in_json_ld:
            self._buffer.append(data)
        if self._current_link is not None:
            self._current_link["text"] += " " + data


def clean_text(value: Any) -> str:
    text = html.unescape(str(value or ""))
    text = re.sub(r"\s+", " ", text).strip()
    return text


def canonical_url(url: str) -> str:
    url, _ = urldefrag(url)
    return url.rstrip("/")


def normalize_start_url(value: str) -> str:
    if os.path.exists(value):
        return os.path.abspath(value).replace("\\", "/")
    parsed = urlparse(value)
    if not parsed.scheme and "." in value:
        return "https://" + value
    return value


def fetch(url: str, timeout: int) -> str:
    target = normalize_start_url(url)
    if os.path.exists(target):
        with open(target, "r", encoding="utf-8") as handle:
            return handle.read()
    request = Request(
        target,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; CodexCompanyJobs/1.0; +https://openai.com)",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    with urlopen(request, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def is_known_ats(url: str) -> bool:
    host = urlparse(url).netloc.lower()
    return any(host == ats or host.endswith("." + ats) for ats in ATS_HOSTS)


def same_site(url: str, root_host: str) -> bool:
    host = urlparse(url).netloc.lower()
    return not host or host == root_host or host.endswith("." + root_host)


def has_career_term(value: str) -> bool:
    lowered = value.lower()
    return any(term in lowered for term in CAREER_TERMS)


def should_crawl(url: str, root_host: str, include_external: bool) -> bool:
    parsed = urlparse(url)
    if parsed.scheme not in {"", "http", "https"}:
        return False
    if same_site(url, root_host):
        return has_career_term(parsed.path) or parsed.path in {"", "/"}
    if include_external and is_known_ats(url):
        return True
    return is_known_ats(url)


def looks_like_job_link(url: str, text: str) -> bool:
    parsed = urlparse(url)
    path = parsed.path.lower()
    lowered_text = clean_text(text).lower()
    if not lowered_text or lowered_text in GENERIC_LINK_TEXT:
        return False
    if len(lowered_text) < 4 or len(lowered_text) > 140:
        return False
    if any(skip in path for skip in ("/blog", "/privacy", "/terms", "/login", "/signup")):
        return False
    if re.search(r"/(job|jobs|opening|position|positions|vacanc|vagas|o|j)/", path):
        return True
    if is_known_ats(url) and not has_career_term(lowered_text):
        return True
    return False


def title_from_link(text: str) -> str:
    text = clean_text(text)
    text = re.sub(r"^(apply for|apply to|view|open|see)\s+", "", text, flags=re.I)
    text = re.sub(r"\s+(apply now|view job|learn more)$", "", text, flags=re.I)
    return clean_text(text)


def flatten_json_ld(value: Any) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    if isinstance(value, list):
        for item in value:
            items.extend(flatten_json_ld(item))
    elif isinstance(value, dict):
        items.append(value)
        if "@graph" in value:
            items.extend(flatten_json_ld(value["@graph"]))
    return items


def type_contains_jobposting(value: Any) -> bool:
    if isinstance(value, list):
        return any(type_contains_jobposting(item) for item in value)
    return str(value).lower() == "jobposting"


def extract_location(value: Any) -> str:
    if isinstance(value, list):
        locations = [extract_location(item) for item in value]
        return ", ".join(item for item in locations if item)
    if not isinstance(value, dict):
        return clean_text(value)
    address = value.get("address", value)
    if isinstance(address, dict):
        parts = [
            address.get("addressLocality"),
            address.get("addressRegion"),
            address.get("addressCountry"),
        ]
        return clean_text(", ".join(str(part) for part in parts if part))
    return clean_text(address)


def jobs_from_json_ld(parser: CareersParser, page_url: str) -> list[Job]:
    jobs: list[Job] = []
    for raw in parser.json_ld:
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            continue
        for item in flatten_json_ld(data):
            if not type_contains_jobposting(item.get("@type")):
                continue
            title = clean_text(item.get("title"))
            if not title:
                continue
            job_url = canonical_url(urljoin(page_url, item.get("url") or page_url))
            employment = item.get("employmentType", "")
            if isinstance(employment, list):
                employment = ", ".join(clean_text(item) for item in employment)
            department = item.get("occupationalCategory") or item.get("industry") or ""
            jobs.append(
                Job(
                    title=title,
                    url=job_url,
                    location=extract_location(item.get("jobLocation") or item.get("applicantLocationRequirements")),
                    department=clean_text(department),
                    employment_type=clean_text(employment),
                    source=page_url,
                )
            )
    return jobs


def jobs_from_links(parser: CareersParser, page_url: str) -> list[Job]:
    jobs: list[Job] = []
    for href, text in parser.links:
        absolute = canonical_url(urljoin(page_url, href))
        if looks_like_job_link(absolute, text):
            jobs.append(Job(title=title_from_link(text), url=absolute, source=page_url))
    return jobs


def parse_page(page_url: str, body: str) -> tuple[list[Job], list[tuple[str, str]]]:
    parser = CareersParser()
    parser.feed(body)
    jobs = jobs_from_json_ld(parser, page_url) + jobs_from_links(parser, page_url)
    links = [(canonical_url(urljoin(page_url, href)), text) for href, text in parser.links]
    return jobs, links


def dedupe_jobs(jobs: list[Job]) -> list[Job]:
    seen: set[tuple[str, str]] = set()
    unique: list[Job] = []
    for job in jobs:
        key = (job.title.lower(), canonical_url(job.url).lower())
        if key in seen:
            continue
        seen.add(key)
        unique.append(job)
    return sorted(unique, key=lambda item: (item.title.lower(), item.location.lower(), item.url))


def crawl(start_url: str, max_pages: int, timeout: int, include_external: bool, delay: float) -> tuple[list[Job], list[str], list[str]]:
    start_url = normalize_start_url(start_url)
    parsed_start = urlparse(start_url if "://" in start_url else "file://" + start_url)
    root_host = parsed_start.netloc.lower()
    queue = [canonical_url(start_url)]
    visited: set[str] = set()
    sources: list[str] = []
    errors: list[str] = []
    jobs: list[Job] = []

    while queue and len(visited) < max_pages:
        url = queue.pop(0)
        if url in visited:
            continue
        visited.add(url)
        try:
            body = fetch(url, timeout)
        except Exception as exc:  # noqa: BLE001 - CLI should report all fetch failures.
            errors.append(f"{url}: {exc}")
            continue
        sources.append(url)
        page_jobs, links = parse_page(url, body)
        jobs.extend(page_jobs)

        prioritized: list[str] = []
        secondary: list[str] = []
        for link_url, link_text in links:
            if link_url in visited or link_url in queue:
                continue
            if not should_crawl(link_url, root_host, include_external):
                continue
            if looks_like_job_link(link_url, link_text):
                continue
            if is_known_ats(link_url):
                prioritized.append(link_url)
            else:
                secondary.append(link_url)
        queue.extend(prioritized + secondary)
        if delay:
            time.sleep(delay)

    return dedupe_jobs(jobs), sources, errors


def render_markdown(jobs: list[Job], sources: list[str], errors: list[str]) -> str:
    lines: list[str] = []
    lines.append(f"Found {len(jobs)} possible job opening(s).")
    lines.append("")
    if jobs:
        lines.extend(["| Title | Location | Department | Type | Link |", "| --- | --- | --- | --- | --- |"])
        for job in jobs:
            lines.append(
                "| {title} | {location} | {department} | {kind} | {url} |".format(
                    title=job.title.replace("|", "\\|"),
                    location=(job.location or "-").replace("|", "\\|"),
                    department=(job.department or "-").replace("|", "\\|"),
                    kind=(job.employment_type or "-").replace("|", "\\|"),
                    url=job.url,
                )
            )
    if sources:
        lines.extend(["", "Sources checked:"])
        lines.extend(f"- {source}" for source in sources)
    if errors:
        lines.extend(["", "Fetch errors:"])
        lines.extend(f"- {error}" for error in errors)
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Find possible openings on a company careers site.")
    parser.add_argument("url", help="Company site, careers page, ATS board URL, or local HTML file path.")
    parser.add_argument("--max-pages", type=int, default=30, help="Maximum pages to crawl. Default: 30.")
    parser.add_argument("--timeout", type=int, default=20, help="Fetch timeout in seconds. Default: 20.")
    parser.add_argument("--include-external", action="store_true", help="Crawl external career-like links, not just known ATS hosts.")
    parser.add_argument("--delay", type=float, default=0.0, help="Delay between requests in seconds. Default: 0.")
    parser.add_argument("--output", choices=("markdown", "json"), default="markdown", help="Output format. Default: markdown.")
    args = parser.parse_args()

    jobs, sources, errors = crawl(args.url, args.max_pages, args.timeout, args.include_external, args.delay)
    if args.output == "json":
        print(json.dumps({"jobs": [asdict(job) for job in jobs], "sources": sources, "errors": errors}, indent=2, ensure_ascii=False))
    else:
        print(render_markdown(jobs, sources, errors))
    return 0 if jobs or sources else 1


if __name__ == "__main__":
    sys.exit(main())
