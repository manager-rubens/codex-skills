#!/usr/bin/env python3
"""Normalize salary observations into monthly and annual estimates."""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import Counter, defaultdict
from typing import Any


def point_value(item: dict[str, Any]) -> float:
    if "value" in item and item["value"] is not None:
        return float(item["value"])
    if "range_min" in item and "range_max" in item:
        return (float(item["range_min"]) + float(item["range_max"])) / 2
    raise ValueError(f"Observation missing value or range: {item}")


def to_monthly_annual(item: dict[str, Any]) -> tuple[float, float]:
    value = point_value(item)
    period = str(item.get("period", "")).lower()
    if period == "monthly":
        return value, value * 12
    if period == "annual":
        return value / 12, value
    raise ValueError(f"Unsupported period {period!r}; use monthly or annual")


def confidence(observations: list[dict[str, Any]]) -> str:
    if not observations:
        return "very_low"

    qualities = [str(o.get("match_quality", "")).lower() for o in observations]
    visibility = [str(o.get("visibility", "")).lower() for o in observations]
    exact = qualities.count("exact")
    strong = exact and any(v == "full" for v in visibility)
    count = len(observations)

    if strong and count >= 2:
        return "high"
    if strong or (count >= 3 and any(q in {"close_role", "benchmark"} for q in qualities)):
        return "medium"
    if count >= 2:
        return "low"
    return "very_low"


def summarize(observations: list[dict[str, Any]]) -> dict[str, Any]:
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in observations:
        buckets[str(item.get("currency", "")).upper()].append(item)

    results = []
    for currency, items in buckets.items():
        monthly_values = []
        annual_values = []
        for item in items:
            monthly, annual = to_monthly_annual(item)
            monthly_values.append(monthly)
            annual_values.append(annual)

        results.append(
            {
                "currency": currency,
                "observation_count": len(items),
                "monthly_mean": round(statistics.fmean(monthly_values), 2),
                "monthly_median": round(statistics.median(monthly_values), 2),
                "annual_mean": round(statistics.fmean(annual_values), 2),
                "annual_median": round(statistics.median(annual_values), 2),
                "confidence": confidence(items),
                "match_quality_counts": dict(Counter(str(i.get("match_quality", "")).lower() for i in items)),
                "sources": [
                    {
                        "source": i.get("source"),
                        "company": i.get("company"),
                        "role": i.get("role"),
                        "url": i.get("url"),
                        "period": i.get("period"),
                        "point_value": point_value(i),
                    }
                    for i in items
                ],
            }
        )

    return {"results": results}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", help="JSON file with salary observations. Reads stdin when omitted.")
    args = parser.parse_args()

    raw = open(args.input, encoding="utf-8").read() if args.input else sys.stdin.read()
    observations = json.loads(raw)
    if not isinstance(observations, list):
        raise SystemExit("Input must be a JSON array of observations")

    print(json.dumps(summarize(observations), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
