#!/usr/bin/env python3
"""Validate a Council report's mechanical contract without making a decision."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED = ("Recomendação", "Evidências", "Premissas", "Dados ausentes", "Confiança", "Score disciplinar", "Condição de abandono", "Próximo experimento")


def validate(text: str) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED:
        if field.lower() not in text.lower():
            errors.append(f"campo ausente: {field}")
    if not re.search(r"\b(?:CONSTRUIR|MUDAR|ESPERAR|MATAR)\b", text):
        errors.append("recomendação deve ser CONSTRUIR, MUDAR, ESPERAR ou MATAR")
    scores = [int(value) for value in re.findall(r"(?:score disciplinar|score)[^\d]{0,20}(\d{1,2})", text, re.I)]
    if any(score > 30 for score in scores):
        errors.append("score disciplinar não pode exceder 30")
    if re.search(r"\b100\s*%\b|100 por cento|certeza absoluta", text, re.I):
        errors.append("não declarar certeza absoluta")
    if "veto" in text.lower() and not re.search(r"desbloque|condição de saída|evidência", text, re.I):
        errors.append("veto precisa de critério de desbloqueio")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    errors = validate(args.report.read_text(encoding="utf-8"))
    if errors:
        print("FALHOU")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASSOU: contrato mecânico do Conselho")
    return 0


if __name__ == "__main__":
    sys.exit(main())
