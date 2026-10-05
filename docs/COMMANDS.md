# Comandos

| Comando | Quando usar | Referência |
|---|---|---|
| `help` | descobrir o fluxo | `SKILL.md` |
| `init` | registrar contexto durável | `references/commands.md` |
| `route` | selecionar cargos e lentes | `references/commands.md` |
| `consult` | pedir uma lente | persona correspondente |
| `debate` | resolver trade-offs | `references/commands.md` |
| `decide` | produzir recomendação completa | `references/output-contract.md` |
| `compare` | avaliar alternativas | `references/commands.md` |
| `audit` | revisar decisão pronta | `references/quality-floor.md` |
| `red-team` | procurar falhas | `references/commands.md` |
| `calibrate` | comparar previsão e resultado | `references/calibration.md` |
| `record` | persistir ADR autorizado | `references/output-contract.md` |
| `doctor` | diagnosticar drift | `references/commands.md` |

## Sintaxe livre

O comando pode ser escrito como `$conselho decide`, `/conselho decide`, `Conselho: decide` ou em linguagem natural. A skill deve reconhecer intenção mesmo quando o harness não possui slash commands.

## Seleção automática

Se o usuário pergunta “qual devo escolher?”, use `decide`. Se pergunta “quem deve analisar?”, use `route`. Se apresenta uma decisão pronta e pede revisão, use `audit`. Se pede para encontrar falhas, use `red-team`. Se informa o resultado de uma decisão anterior, use `calibrate`.
