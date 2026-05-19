# Complement: claus de respostes 2026

Aquest mini-ZIP afegeix 4 fitxers que mancaven al repo per consistència amb
els del 2025 ja integrats:

```
data/CAN-1ESO-2026-answers.json   NOU (clau oficial 2026, 30 entrades)
data/CAN-2ESO-2026-answers.json   NOU
data/CAN-3ESO-2026-answers.json   NOU
data/CAN-4ESO-2026-answers.json   NOU
```

Cap fitxer existent se sobreescriu. Descomprimeix sobre l'arrel del repo.

## Validació

Les 120 entrades coincideixen amb totes les `resposta_correcta` del catàleg
2026 als `problems_<n>eso.py` actuals. Si en algun moment futur algú edita
una `resposta_correcta` del 2026 sense voler, una simple comprovació catàleg
↔ JSON ho detectarà — que és precisament el motiu pel qual aquests fitxers
existeixen.

— Agent X (correcció)
