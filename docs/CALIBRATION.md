# Calibração

Congele a previsão antes do resultado: decisão, recomendação, confiança, evidências, dissenso e condições de abandono. Depois registre `correct` com critério definido previamente.

```bash
python scripts/calibrate_decision.py evals/calibration.sample.json
```

O script calcula quantidade, acurácia observada, confiança média, Brier score e diferença absoluta entre confiança média e acurácia. Isso descreve apenas o dataset rotulado; não prova desempenho futuro nem transforma a confiança em probabilidade válida.
