#!/usr/bin/env python3
"""Calculate descriptive calibration metrics from labelled decision outcomes."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def metrics(items: list[dict]) -> dict:
    if not items:
        return {"n": 0, "accuracy": None, "mean_confidence": None, "brier": None, "calibration_gap": None}
    confidences = [max(0.0, min(1.0, float(x["confidence"]) / 100)) for x in items]
    outcomes = [1.0 if bool(x["correct"]) else 0.0 for x in items]
    return {
        "n": len(items),
        "accuracy": sum(outcomes) / len(items),
        "mean_confidence": sum(confidences) / len(items),
        "brier": sum((p - y) ** 2 for p, y in zip(confidences, outcomes)) / len(items),
        "calibration_gap": abs(sum(confidences) / len(items) - sum(outcomes) / len(items)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.file.read_text(encoding="utf-8"))
    if isinstance(payload, dict) and "items" not in payload:
        raise SystemExit("Entrada inválida: use {\"items\":[{\"confidence\": 0-100, \"correct\": true|false}]}.")
    items = payload["items"] if isinstance(payload, dict) else payload
    result = metrics(items)
    result["warning"] = "Métricas descritivas do conjunto rotulado; não garantem desempenho futuro."
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
