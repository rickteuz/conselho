import json
from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_plugin_manifest_points_to_existing_files():
    manifest = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    assert manifest["name"] == "conselho"
    assert manifest["skills"] == "./.claude/skills/"
    assert (ROOT / "plugin" / "agents").exists()


def test_source_of_truth_has_required_layers():
    for relative in ("SKILL.md", "personas", "knowledge", "references", "scripts", "tests", "docs", "plugin", "schemas", "evals"):
        assert (ROOT / relative).exists()


def test_rag_index_references_all_personas_and_cards():
    index = (ROOT / "knowledge" / "index.yaml").read_text(encoding="utf-8")
    for persona_id in ("jeff-bezos", "warren-buffett", "ray-dalio", "steve-jobs", "sam-altman", "alex-hormozi"):
        assert persona_id in index
    for card_id in ("JB-01", "JB-02", "JB-03", "JB-04", "JB-05", "JB-06", "WB-01", "WB-02", "WB-03", "WB-04", "WB-05", "WB-06", "RD-01", "RD-02", "RD-03", "RD-04", "RD-05", "RD-06", "SJ-01", "SJ-02", "SJ-03", "SJ-04", "SJ-05", "SJ-06", "SA-01", "SA-02", "SA-03", "SA-04", "SA-05", "SA-06", "AH-01", "AH-02", "AH-03", "AH-04", "AH-05", "AH-06"):
        assert card_id in index


def test_distribution_contains_rag_index():
    dist = ROOT / "dist"
    indexes = list(dist.glob("*/**/knowledge/index.yaml"))
    assert len(indexes) >= 4


def test_retriever_returns_relevant_cards():
    import sys
    sys.path.insert(0, str(ROOT / "scripts"))
    from retrieve_knowledge import retrieve
    assert retrieve("dor do cliente e proposta", "jeff-bezos", None, 3)[0]["id"] in {"JB-01", "JB-04", "JB-05"}
    assert retrieve("margem segurança oportunidade", "warren-buffett", None, 3)


def test_source_ledger_has_primary_sources_for_every_persona():
    ledger = (ROOT / "knowledge" / "sources.yaml").read_text(encoding="utf-8")
    for persona_id in ("jeff-bezos", "warren-buffett", "ray-dalio", "steve-jobs", "sam-altman", "alex-hormozi"):
        assert f"persona: {persona_id}" in ledger
    assert ledger.count("url: https://") >= 12


if __name__ == "__main__":
    test_plugin_manifest_points_to_existing_files()
    test_source_of_truth_has_required_layers()
    test_rag_index_references_all_personas_and_cards()
    test_distribution_contains_rag_index()
    test_source_ledger_has_primary_sources_for_every_persona()
    print("PASSOU: testes de estrutura do repositório")
