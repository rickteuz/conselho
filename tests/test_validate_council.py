import importlib.util
from pathlib import Path


ROOT = Path(__file__).parents[1]
SPEC = importlib.util.spec_from_file_location("validate_council", ROOT / "scripts" / "validate_council.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


VALID = """
### Parecer — Bezos
- Recomendação: CONSTRUIR
- Evidências: fonte primária, 2026
- Premissas: hipótese testável
- Dados ausentes: nenhum
- Condição de abandono: parar se métrica cair
- Próximo experimento: teste reversível
- Confiança: 72
- Score disciplinar: 24
"""


def test_valid_contract_passes():
    assert MODULE.validate(VALID) == []


def test_missing_evidence_fails():
    errors = MODULE.validate(VALID.replace("Evidências: fonte primária, 2026", ""))
    assert any("Evidências" in error for error in errors)


def test_impossible_score_fails():
    errors = MODULE.validate(VALID.replace("Score disciplinar: 24", "Score disciplinar: 31"))
    assert any("exceder 30" in error for error in errors)


def test_all_builtin_personas_are_present():
    expected = {"jeff-bezos", "warren-buffett", "ray-dalio", "steve-jobs", "sam-altman", "alex-hormozi"}
    actual = {path.stem for path in (ROOT / "personas").glob("*.md") if path.name != "README.md"}
    assert actual == expected
    for persona_id in expected:
        content = (ROOT / "personas" / f"{persona_id}.md").read_text(encoding="utf-8")
        for field in ("id", "role", "status", "confidence"):
            assert f"{field}:" in content
        for heading in ("## Missão", "## Perguntas", "## Aprova quando", "## Veta quando", "## Vieses a controlar", "## Contrapesos"):
            assert heading in content


if __name__ == "__main__":
    test_valid_contract_passes()
    test_missing_evidence_fails()
    test_impossible_score_fails()
    test_all_builtin_personas_are_present()
    print("PASSOU: testes do validador do Conselho")
