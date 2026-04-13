# FAQ

## Che differenza c'è tra `examples`, `community` e `verified`?
- `examples/` contiene esempi didattici o dimostrativi
- `community/` contiene script condivisi dalla community ma non ancora verificati formalmente da AMV
- `verified/` contiene script revisionati e verificati da AMV

## Come faccio a capire se uno script è affidabile?
Controlla in quale cartella si trova, la versione di MasterSap su cui è stato testato e le limitazioni dichiarate nell'header.

## Cosa deve contenere ogni script?
Ogni script deve includere un header completo
```python
# ============================================================
# MasterSap Script
# Titolo: <titolo breve>
# Autore: <nome / nick>
# Licenza: Apache-2.0
# Testato su: MasterSap YYYY ReleaseNumber <es. MasterSap 2026 R1 / MasterSap 2026 R2 ...>
# Unità: <kg | kN; cm | m>
# Scopo: <cosa fa lo script in 1-3 righe>
# Input: <parametri, file richiesti, assunzioni>
# Output: <cosa crea/modifica in MasterSap>
# Limitazioni: <vincoli noti, casi non gestiti, performance, ecc.>
# ============================================================
```

## Posso caricare uno script con dati di un cliente?
No. I contributi non devono contenere dati sensibili, riservati o riferimenti a progetti di clienti.

## Dove metto uno script nuovo?
- in `examples/` se è un esempio didattico
- in `community/` se è un contributo utile ma non ancora verificato
- in `verified/` solo dopo verifica interna

## Come faccio a proporre miglioramenti?
Apri una issue o una pull request e descrivi chiaramente cosa cambia e perché.

## Uno script community può diventare verified?
Sì, dopo revisione tecnica e verifica interna.

## Posso usare direttamente uno script in produzione?
Solo dopo averlo verificato nel tuo ambiente. Anche gli script verified vanno usati con consapevolezza rispetto al contesto operativo.
