#!/usr/bin/env python3
"""Build provider-neutral distribution folders from the Council source of truth."""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIRS = ("personas", "knowledge", "references")
SOURCE_FILES = ("SKILL.md", "README.md", "VERSION")
RUNTIME_SCRIPTS = ("retrieve_knowledge.py", "validate_council.py", "calibrate_decision.py")
PROVIDERS = {
    "agents": ".agents/skills/conselho",
    "claude": ".claude/skills/conselho",
    "codex": ".agents/skills/conselho",
    "gemini": ".gemini/skills/conselho",
}


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))


def build(out: Path) -> list[Path]:
    generated: list[Path] = []
    for provider, relative in PROVIDERS.items():
        provider_root = out / provider
        if provider_root.exists():
            shutil.rmtree(provider_root)
        target = out / provider / relative
        target.mkdir(parents=True, exist_ok=True)
        for name in SOURCE_FILES:
            shutil.copy2(ROOT / name, target / name)
        for directory in SOURCE_DIRS:
            copy_tree(ROOT / directory, target / directory)
        (target / "scripts").mkdir(parents=True, exist_ok=True)
        for script in RUNTIME_SCRIPTS:
            shutil.copy2(ROOT / "scripts" / script, target / "scripts" / script)
        shutil.copy2(ROOT / "agents" / "openai.yaml", target / "agents-openai.yaml")
        generated.append(target)

    plugin = out / "plugin"
    plugin.mkdir(parents=True, exist_ok=True)
    copy_tree(ROOT / "plugin" / "agents", plugin / "agents")
    copy_tree(ROOT / "personas", plugin / ".claude" / "skills" / "conselho" / "personas")
    copy_tree(ROOT / "knowledge", plugin / ".claude" / "skills" / "conselho" / "knowledge")
    copy_tree(ROOT / "references", plugin / ".claude" / "skills" / "conselho" / "references")
    for name in SOURCE_FILES:
        shutil.copy2(ROOT / name, plugin / ".claude" / "skills" / "conselho" / name)
    shutil.copy2(ROOT / ".claude-plugin" / "plugin.json", plugin / "plugin.json")
    generated.append(plugin)
    return generated


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    paths = build(args.out)
    print(f"PASSOU: {len(paths)} pacotes gerados em {args.out}")
    for path in paths:
        print(f"- {path.relative_to(args.out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
