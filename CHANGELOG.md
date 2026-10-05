# Changelog

## 2.3.0 — 2026-10-05

- Adicionada Knowledge Base RAG embutida com índice por tags e 18 cartões atômicos.
- Cada persona ganhou cartões com tese, contexto, perguntas, teste, contraexemplo, veto, viés e fonte.
- O fluxo agora recupera contexto seletivo e exige IDs de evidência no parecer.

## 2.2.0 — 2026-10-05

- Reestruturado como repositório multi-harness com `docs/`, `plugin/agents/`, `.claude-plugin/`, `dist/` e builder reproduzível.
- README reescrito como documentação de produto, instalação, uso, arquitetura e limites.
- Adicionados agentes independentes de análise, red-team e síntese.
- Adicionados testes de estrutura e distribuição.

## 2.0.0 — 2026-10-05

- Reestruturado como sistema portátil de governança decisória.
- Adicionados comandos de roteamento, consulta, debate, decisão, comparação, auditoria, red-team, calibração, registro e doctor.
- Adicionados contratos de saída, piso de qualidade e playbooks.
- Adicionado validador determinístico de relatórios.
- Adicionado mapa de fontes canônicas e documentação de instalação universal.

## 2.1.0 — 2026-10-05

- Personas completas incorporadas em `personas/`, tornando o pacote funcional sem acesso ao vault.
- Cada persona recebeu missão, domínio, princípios, perguntas, aprovação, veto, vieses, contrapesos, fontes e limitações.
- Documentação pública atualizada para separar conteúdo embutido de fontes opcionais do vault.

## 1.0.0

- Primeira versão com as seis lentes executivas e matriz de confiabilidade.
## 2.4.0 — RAG executável e distribuição endurecida

- adicionados 18 cartões de conhecimento, totalizando 36 cartões citáveis;
- incluído recuperador local determinístico, script de calibração e casos de avaliação;
- adicionados schemas de pacote de decisão e dataset de calibração;
- corrigido manifesto Claude e distribuição Codex para `.agents/skills/`;
- builder agora copia apenas runtime necessário e inclui `agents/openai.yaml`;
- adicionada validação contínua para GitHub Actions.
