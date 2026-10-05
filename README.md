# Conselho

### A decision-making skill that makes trade-offs visible.

O Conselho é uma skill pública e portátil para transformar decisões difíceis em recomendações auditáveis. Ele combina seis lentes executivas, pareceres independentes, debate controlado, red-team, vetos desbloqueáveis, score disciplinar e calibração contra resultados reais.

> **Não é um chatbot que “dá opinião”.** É um protocolo de decisão que mostra quem está analisando, quais evidências sustentam a tese, onde estão os riscos e o que faria a recomendação mudar.

## Por que usar

Decisões ruins raramente falham por falta de inteligência. Elas falham porque:

- a pergunta já contém uma solução enviesada;
- fatos e preferências são misturados;
- a alternativa de não agir é esquecida;
- um único ponto de vista domina;
- risco é discutido sem dono ou condição de parada;
- confiança é confundida com probabilidade de acerto;
- a equipe não congela a previsão para aprender com o resultado.

O Conselho foi desenhado para atacar esses pontos sem transformar uma escolha em burocracia infinita.

## Em 30 segundos

```text
Use o Conselho para decidir entre lançar em 30 dias ou construir a versão completa em 90 dias.
Contexto: dois desenvolvedores, 200 usuários, orçamento de R$ 10 mil.
Critério de sucesso: validar demanda sem comprometer caixa.
Não execute nada; entregue apenas a análise.
```

O agente deve rotear para produto, cliente, capital e risco; produzir pareceres separados; comparar custo, aprendizado e downside; registrar dissenso; emitir um veredito; e deixar explícito que a execução continua dependendo de autorização humana.

## Instalação

### Qualquer IA com suporte a skills Markdown

Copie esta pasta para o diretório de skills do agente. O arquivo obrigatório é `SKILL.md`; `personas/` e `references/` são parte do comportamento, não documentação opcional.

### Distribuições incluídas

```text
dist/agents/   Codex, agentes compatíveis com .agents/
dist/claude/   Claude Code
dist/codex/    Codex project-local (.agents/skills/)
dist/gemini/   Gemini CLI
dist/plugin/   agentes do plugin
```

Para recriar as distribuições:

```bash
python scripts/build_distribution.py
```

O builder é determinístico e sempre parte dos arquivos de fonte. Não edite `dist/` manualmente.

## Como usar

Os comandos funcionam como linguagem de roteamento, mesmo quando o harness não possui slash commands:

```text
$conselho help
$conselho init
$conselho route: quem deve analisar esta decisão?
$conselho consult: analise pela lente de Buffett
$conselho debate: compare as alternativas
$conselho decide: qual caminho devemos seguir?
$conselho compare: contratar ou desenvolver internamente?
$conselho audit: revise esta recomendação
$conselho red-team: tente falsificar esta tese
$conselho calibrate: compare a previsão com o resultado
$conselho record: registre esta decisão como ADR
$conselho doctor: verifique o estado da base decisória
```

Se o comando não for informado, a skill reconhece a intenção em linguagem natural e escolhe o fluxo adequado.

## As seis lentes

| Lente | Pergunta dominante | Veto típico |
|---|---|---|
| **Jeff Bezos** | Existe uma dor real de cliente? | Solução sem cliente, evidência ou experimento |
| **Warren Buffett** | Esta alocação cria valor com margem de segurança? | Capital sem retorno ou custo de oportunidade estimável |
| **Ray Dalio** | O que pode falhar e como paramos? | Risco crítico sem controle, dono ou parada |
| **Steve Jobs** | O que é essencial e o que deve ser removido? | Excesso, indiferenciação ou tecnologia sem problema |
| **Sam Altman** | Qual vantagem se acumula e qual o próximo experimento? | Ambição sem mecanismo testável |
| **Alex Hormozi** | A oferta é desejável, provável, rápida e entregável? | Promessa não demonstrável ou economia insustentável |

As personas completas estão em [`personas/`](personas/). Cada uma possui missão, domínio, princípios, perguntas, critérios, vieses, contrapesos, fontes e limitações.

## Fluxo de decisão

```text
pergunta
  ↓
pacote de decisão
  ↓
roteamento de cargos e personas
  ↓
pareceres independentes
  ↓
debate + red-team
  ↓
matriz de trade-offs + vetos
  ↓
veredito limitado
  ↓
ação autorizada + métrica + revisão
  ↓
calibração contra o resultado
```

## O que uma resposta precisa conter

Uma decisão completa informa objetivo, alternativas, escopos, reversibilidade, evidências, dados ausentes, pareceres, premissas, dissensos, vetos, score, confiança, ação autorizada, dono, métrica, condição de parada e data de revisão. O schema está em [`references/output-contract.md`](references/output-contract.md).

## Segurança epistemológica

- As personas são lentes baseadas em padrões públicos, não simulações literais de pessoas reais.
- `DRAFT / NÃO CALIBRADA` reduz confiança, mas não impede análise.
- Score disciplinar mede qualidade do processo; não é porcentagem de acerto.
- Veto crítico não é superado por votação ou média.
- Dados ausentes viram `PENDENTE`, não são inventados.
- O Conselho recomenda; a pessoa responsável autoriza execução.

## Arquitetura

| Diretório | Responsabilidade |
|---|---|
| `SKILL.md` | contrato principal e roteador |
| `personas/` | conhecimento das seis lentes |
| `knowledge/` | corpus RAG atômico com índice, tags e IDs citáveis |
| `references/` | playbooks e contratos progressivos |
| `plugin/agents/` | analista, red-team e sintetizador delegáveis |
| `scripts/` | builder e validação determinística |
| `tests/` | regressões do contrato e da distribuição |
| `docs/` | arquitetura, comandos, instalação e personas |
| `dist/` | pacotes gerados por harness |

Leia [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) para entender a separação entre fonte e distribuição.

## RAG embutido

O corpus em `knowledge/` não é um texto decorativo. `index.yaml` roteia domínio e tags para 36 cartões atômicos, seis por persona. O utilitário local `scripts/retrieve_knowledge.py` faz recuperação determinística por sobreposição semântica leve, filtro por persona/tag e saída JSON ou Markdown. Cada cartão contém tese, contexto de uso, perguntas, teste, veto e fonte. Em uma decisão normal, o agente recupera apenas os cartões relevantes e cita seus IDs; isso reduz tokens e melhora rastreabilidade.

## Desenvolvimento

```bash
python scripts/build_distribution.py
python tests/test_validate_council.py
python tests/test_repository.py
python scripts/validate_council.py references/output-contract.md
python scripts/retrieve_knowledge.py "risco operacional e margem" --limit 5
```

Os testes validam o contrato mecânico, a presença das seis personas, o manifesto do plugin e as camadas do repositório. Eles não provam que uma recomendação real está correta.

## Limites

O Conselho não substitui aconselhamento jurídico, médico, financeiro ou profissional; não publica, compra, envia, exclui ou altera produção sozinho; e não promete acerto, certeza ou segurança absoluta.

## Licença e publicação

Este projeto é distribuído sob a licença [MIT](LICENSE). Antes de publicar, revise as fontes públicas das personas e mantenha as limitações epistemológicas descritas neste README. O pacote é independente e pode ser publicado como um repositório próprio.
