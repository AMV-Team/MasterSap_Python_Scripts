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
   - Elementi trave: attenzione a segmenti troppo corti (es. lunghezze minime in funzione della scala del modello)
   - Elementi guscio/macro: attenzione a spessore minimo e distanze minime tra nodi
5) **ID univoci**: gli ID devono essere univoci.
6) **Nessun dato cliente**: non caricare modelli reali, nomi, indirizzi, log o file contenenti dati identificativi.

> Le regole dettagliate sono in `docs/style-guide.md`.

## Header obbligatorio (in cima a ogni script)
Ogni script deve iniziare con:

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
