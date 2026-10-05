# Arquitetura do Conselho

## Objetivo

O Conselho é uma skill de governança decisória, não um personagem único. Seu desenho separa conhecimento, roteamento, execução, persistência e distribuição para que o mesmo contrato funcione em agentes diferentes.

## Camadas

```text
SKILL.md                 contrato de entrada, roteamento e invariantes
personas/                seis lentes completas e versionadas
knowledge/               cartões RAG atômicos, índice e tags de recuperação
references/              playbooks, schemas, qualidade e calibração
plugin/agents/           papéis delegáveis para análise independente
scripts/                 validação e build reproduzível
tests/                   regressões do contrato e da distribuição
docs/                    documentação pública e decisões de arquitetura
dist/                    pacotes gerados para harnesses compatíveis
```

## Fonte de verdade

O diretório raiz é a fonte editável. `dist/` é saída gerada e pode ser recriado pelo builder. Nunca edite manualmente uma cópia em `dist/` para corrigir o comportamento; altere `SKILL.md`, `personas/`, `references/` ou `plugin/` e gere novamente.

## Protocolo de execução

1. O agente reconhece a intenção e escolhe um comando.
2. O comando carrega somente o playbook necessário.
3. O roteador escolhe uma lente primária e contrapesos.
4. Analistas independentes produzem pareceres sem ver uns aos outros.
5. O sintetizador compara premissas, evidências, vetos e trade-offs.
6. O contrato de saída produz veredito limitado, revisão e autorização.
7. O registro só é persistido quando o usuário autoriza.

## Modos de execução

- **Standalone:** um agente lê `SKILL.md`, personas e referências.
- **Multi-agent:** `plugin/agents/` separa análise, red-team e síntese.
- **Vault-aware:** fontes privadas atualizam contexto sem substituir o núcleo público.
- **Offline:** funciona com os arquivos distribuídos, sem API ou internet.

## Regras de degradação

Se agentes paralelos não estiverem disponíveis, execute no mesmo contexto e escreva `DEGRADADO: análise não isolada`. Se fontes canônicas não estiverem disponíveis, use as personas embutidas e marque a evidência como portátil. Se persistência não for possível, entregue o ADR na resposta sem afirmar que foi gravado.
