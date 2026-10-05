# Começando com o Conselho

## Instalação manual

Copie a pasta para o diretório de skills do seu agente. O mínimo necessário é:

```text
conselho/
├── SKILL.md
├── personas/
└── references/
```

Depois reinicie ou recarregue o agente e peça:

```text
Use o Conselho para decidir entre [alternativa A] e [alternativa B].
Contexto: [...]
Restrições: [...]
```

## Instalação por distribuição

Execute o builder para gerar cópias compatíveis:

```bash
python scripts/build_distribution.py
```

As saídas aparecem em `dist/agents`, `dist/claude`, `dist/codex`, `dist/gemini` e `dist/plugin`.

## Primeiro uso

```text
$conselho help
$conselho init
$conselho route: devo contratar ou construir internamente?
$conselho decide: qual alternativa devo executar?
```

## Bom briefing

Inclua problema, objetivo, alternativas, prazo, orçamento, restrições, riscos conhecidos, critério de sucesso e o que o agente está autorizado a fazer. Se algo não for conhecido, escreva `PENDENTE`; não peça que a IA preencha a lacuna.

## Exemplos

### Produto

```text
Use $conselho debate. Precisamos decidir se lançamos uma versão simples em 30 dias ou uma versão completa em 90 dias. Temos dois desenvolvedores, orçamento limitado e uma base pequena de usuários.
```

### Capital

```text
Use $conselho compare. Compare investir R$ 10 mil em aquisição, produto ou reserva. Mostre custo de oportunidade, downside e experimento reversível.
```

### Red team

```text
Use $conselho red-team nesta recomendação. Procure premissas ocultas, efeitos de segunda ordem e condições de abandono.
```

## O que o Conselho não faz

Não dá autorização jurídica, financeira ou operacional; não imita pessoas reais; não transforma score em probabilidade; não publica, compra, envia, exclui ou altera produção automaticamente.
