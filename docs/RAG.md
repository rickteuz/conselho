# RAG local do Conselho

O corpus está em `knowledge/personas/` e o catálogo em `knowledge/index.yaml`. Cada cartão tem ID estável, tags, tese, uso, perguntas, teste, veto e fonte.

## Recuperar

```bash
python scripts/retrieve_knowledge.py "qual risco operacional devo controlar" --limit 5
python scripts/retrieve_knowledge.py "margem e oportunidade" --persona warren-buffett --format json
```

O recuperador é local, determinístico e deliberadamente simples: tokeniza a pergunta, calcula sobreposição com cada cartão e permite filtro de persona/tag. Ele não é um embedding store e não deve ser descrito como busca semântica profunda. Se nada for recuperado, a saída é `NÃO TENHO BASE SUFICIENTE`.

## Política de uso

Use de 3 a 7 cartões da lente primária e pelo menos 2 contrapesos em decisões multi-eixo. Cite os IDs na análise. Nunca trate score de recuperação como confiança da decisão.
