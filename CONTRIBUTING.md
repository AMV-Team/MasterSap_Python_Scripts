# Contributing Guide

Grazie per voler contribuire! Questo repository raccoglie **script Python** per MasterSap.

## Dove discutere cosa
- **Domande, consigli, brainstorming:** usa **Discussions**
- **Bug riproducibili / richieste specifiche:** apri una **Issue**
- **Modifiche a script/documentazione:** invia una **Pull Request**

## Tipi di contributo
- Nuovi script in `community/`
- Miglioramenti a `examples/`
- Fix e manutenzione di `verified/` (solo via PR, con review)

## Regole di base per gli script
1) **Solo ASCII**: gli script devono contenere solo caratteri ASCII.  
2) **Unità esplicita**: ogni script deve dichiarare l’unità (m o cm) e mantenere coerenza.  
3) **Numeri float**: quando usi float, usa il **punto** come separatore decimale (`30.0`, non `30,0`).  
4) **Vincoli geometrici** (quando applicabili):
   - travi: attenzione a segmenti troppo corti (es. lunghezze minime in funzione della scala del modello)
   - piastre: spessore minimo e distanze minime tra nodi
5) **ID univoci**: se gestisci tu gli ID, devono essere univoci; in alternativa lascia che sia MasterSap a generarli (se supportato).
6) **Nessun dato cliente**: non caricare modelli reali, nomi, indirizzi, log o file contenenti dati identificativi.

> Le regole dettagliate sono in `docs/style-guide.md`.

## Header obbligatorio (in cima a ogni script)
Ogni script deve iniziare con:

```python
# MasterSap Script
# Title: ...
# Author: ...
# License: Apache-2.0
# Tested on: MasterSap YYYY (build/patch if known)
# Units: m / cm
# Purpose: ...
# Inputs: ...
# Output: ...
# Limitations: ...
