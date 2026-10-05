---
resumo: Corpus RAG embutido do Conselho, organizado em cartões atômicos recuperáveis.
---

# Knowledge Base do Conselho

Esta pasta é o banco de conhecimento portátil das personas. Cada cartão tem um ID estável, tags, tese, uso, teste, contraindicação e fonte. O agente deve recuperar cartões relevantes; não deve despejar todos os arquivos no contexto.

`sources.yaml` é o registro de fontes primárias e dos conceitos que cada fonte sustenta. A lista não transforma uma fonte em verdade universal: ela informa proveniência e ajuda a localizar atualização ou conflito.

## Política de recuperação

1. Extraia do pedido: domínio, decisão, horizonte, recurso escasso, risco e tipo de evidência.
2. Consulte `index.yaml` por tags, IDs e roteamento.
3. Leia de 3 a 7 cartões da lente primária e pelo menos 2 cartões de contrapeso quando a decisão for multi-eixo.
4. Se dois cartões conflitarem, preserve ambos, indique contexto e envie o conflito para o debate.
5. Cite os IDs dos cartões usados no parecer.
6. Se nenhum cartão cobrir a pergunta, declare `NÃO TENHO BASE SUFICIENTE` e proponha pesquisa ou experimento.

## Qualidade

O corpus distingue `evidência`, `interpretação operacional`, `heurística`, `contraexemplo` e `limite`. Fontes públicas são contexto, não prova de que a recomendação dará certo no caso atual.
