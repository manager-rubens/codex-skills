#!/usr/bin/env python3
"""Extract public e-SAJ case listings/details from saved HTML files."""

from __future__ import annotations

import argparse
import glob
import html
import json
import os
import re
from typing import Any


def clean(value: str | None) -> str:
    if not value:
        return ""
    value = re.sub(r"<br\s*/?>", " | ", value, flags=re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    value = value.replace("\xa0", " ")
    return re.sub(r"\s+", " ", value).strip()


def by_id(source: str, element_id: str) -> str:
    match = re.search(r'id="' + re.escape(element_id) + r'"[^>]*>(.*?)</', source, re.S)
    return clean(match.group(1)) if match else ""


def first_class(source: str, class_name: str) -> str:
    match = re.search(r'class="' + re.escape(class_name) + r'">(.*?)</div>', source, re.S)
    return match.group(1) if match else ""


def extract_parties(source: str) -> list[dict[str, str]]:
    parties: list[dict[str, str]] = []
    for row in re.findall(r'<tr class="fundoClaro">(.*?)</tr>', source, re.S):
        role = re.search(r'tipoDeParticipacao">(.*?)</span>', row, re.S)
        name = re.search(r'<td class="nomeParteEAdvogado".*?>(.*?)</td>', row, re.S)
        if role and name:
            parties.append({"role": clean(role.group(1)), "name": clean(name.group(1))})
    return parties


def extract_movements(source: str, limit: int) -> list[dict[str, str]]:
    movements: list[dict[str, str]] = []
    pattern = r'<tr class="(?:fundoClaro|fundoEscuro) containerMovimentacao".*?>(.*?)</tr>'
    for row in re.findall(pattern, source, re.S)[:limit]:
        date = re.search(r'class="dataMovimentacao"[^>]*>(.*?)</td>', row, re.S)
        desc = re.search(r'class="descricaoMovimentacao"[^>]*>(.*?)</td>', row, re.S)
        if date and desc:
            movements.append({"date": clean(date.group(1)), "description": clean(desc.group(1))})
    return movements


def extract_search_results(source: str) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    current_forum = ""
    chunks = re.split(r'(<h2 class="unj-subtitle[^"]* foroDosProcessos">.*?</h2>)', source, flags=re.S)
    for chunk in chunks:
        if "foroDosProcessos" in chunk:
            current_forum = clean(chunk)
            continue
        for item in re.findall(r"<li>(.*?)</li>", chunk, re.S):
            link = re.search(r'<a href="([^"]+)" class="linkProcesso">\s*([^<]+)</a>', item, re.S)
            if not link:
                continue
            participation = re.search(
                r'tipoDeParticipacao">\s*([^<]+)</label>.*?nomeParte">\s*(.*?)\s*</div>',
                item,
                re.S,
            )
            results.append(
                {
                    "number": clean(link.group(2)),
                    "href": html.unescape(link.group(1)),
                    "forum": current_forum,
                    "party_role": clean(participation.group(1)) if participation else "",
                    "party_name": clean(participation.group(2)) if participation else "",
                    "class": clean(first_class(item, "classeProcesso")),
                    "subject": clean(first_class(item, "assuntoPrincipalProcesso")),
                    "received": clean(first_class(item, "dataLocalDistribuicaoProcesso")),
                }
            )
    return results


def parse_file(path: str, movement_limit: int) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8", errors="ignore") as handle:
        source = handle.read()

    search_results = extract_search_results(source)
    number = by_id(source, "numeroProcesso")
    if search_results and not number:
        return {"file": os.path.abspath(path), "type": "search_results", "results": search_results}

    return {
        "file": os.path.abspath(path),
        "type": "case_detail",
        "number": number,
        "status": by_id(source, "labelSituacaoProcesso"),
        "class": by_id(source, "classeProcesso"),
        "area": by_id(source, "areaProcesso"),
        "subject": by_id(source, "assuntoProcesso"),
        "forum": by_id(source, "foroProcesso"),
        "court": by_id(source, "varaProcesso"),
        "distribution": by_id(source, "dataHoraDistribuicaoProcesso"),
        "value": by_id(source, "valorAcaoProcesso"),
        "judge": by_id(source, "juizProcesso"),
        "parties": extract_parties(source),
        "movements": extract_movements(source, movement_limit),
    }


def expand_paths(patterns: list[str]) -> list[str]:
    paths: list[str] = []
    for pattern in patterns:
        matches = glob.glob(pattern)
        paths.extend(matches if matches else [pattern])
    return sorted(dict.fromkeys(paths))


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract saved e-SAJ HTML data.")
    parser.add_argument("paths", nargs="+", help="HTML file paths or glob patterns")
    parser.add_argument("--json", dest="json_path", help="Write JSON output to this path")
    parser.add_argument("--movement-limit", type=int, default=5, help="Recent movements per case")
    args = parser.parse_args()

    data = [parse_file(path, args.movement_limit) for path in expand_paths(args.paths)]
    output = json.dumps(data, ensure_ascii=False, indent=2)
    if args.json_path:
        with open(args.json_path, "w", encoding="utf-8") as handle:
            handle.write(output + "\n")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
