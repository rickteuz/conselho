#!/usr/bin/env python3
"""Retrieve compact, citeable council cards using a deterministic local scorer."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge" / "personas"
STOP = {"para", "com", "uma", "que", "dos", "das", "por", "não", "como", "qual", "when", "what", "with", "the", "and", "from"}


def tokens(text: str) -> set[str]:
    return {x for x in re.findall(r"[a-zA-ZÀ-ÿ0-9][a-zA-ZÀ-ÿ0-9-]{2,}", text.lower()) if x not in STOP}


def parse_cards() -> list[dict]:
    cards = []
    for path in sorted(KNOWLEDGE.glob("*.md")):
        persona = path.stem
        current = None
        for line in path.read_text(encoding="utf-8").splitlines():
            match = re.match(r"^##\s+([A-Z]{2}-\d+)\s+—\s+(.+)$", line)
            if match:
                if current:
                    cards.append(current)
                current = {"id": match.group(1), "title": match.group(2).strip(), "persona": persona, "text": ""}
            elif current and not line.startswith("---"):
                current["text"] += line + "\n"
        if current:
            cards.append(current)
    return cards


def retrieve(query: str, persona: str | None, tag: str | None, limit: int) -> list[dict]:
    wanted = tokens(query)
    output = []
    for card in parse_cards():
        if persona and card["persona"] != persona:
            continue
        haystack = tokens(card["id"] + " " + card["title"] + " " + card["text"])
        score = len(wanted & haystack)
        if persona and card["persona"] == persona:
            score += 3
        if tag and tag.lower() in card["text"].lower():
            score += 4
        if score:
            card = {**card, "score": score, "citation": f"[{card['id']}]"}
            output.append(card)
    output.sort(key=lambda item: (-item["score"], item["id"]))
    return output[: max(1, limit)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Pergunta ou contexto da decisão")
    parser.add_argument("--persona", help="Filtra por slug da persona")
    parser.add_argument("--tag", help="Dá peso a um marcador")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    args = parser.parse_args()
    results = retrieve(args.query, args.persona, args.tag, args.limit)
    if args.format == "json":
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        if not results:
            print("NÃO TENHO BASE SUFICIENTE: nenhum cartão local foi recuperado.")
        for card in results:
            print(f"- {card['citation']} {card['title']} — {card['persona']} (score {card['score']})")
            compact = " ".join(x.strip() for x in card["text"].splitlines() if x.strip())
            print(f"  {compact[:420]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
