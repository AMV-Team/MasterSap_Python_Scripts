# MasterSap Script Style Guide

Questa guida definisce alcune regole pratiche per scrivere script affidabili.

## 1) Compatibilità e riproducibilità
- Dichiarare sempre la versione MasterSap testata
- Dichiarare le unità utilizzate (m o cm)
- Evitare dipendenze esterne non necessarie

## 2) Formato e caratteri
- Solo caratteri ASCII (no accentate, emoji, simboli non ASCII)

## 3) Numeri e formati
- Per i float usare il separatore decimale `.` (punto), non la virgola

## 4) Modellazione: vincoli tipici
> Nota: i vincoli specifici dipendono dalla scala del modello e dalle regole di import/elaborazione.
- Attenzione alle travi troppo corte in caso di spezzamenti/intersezioni
- Piastre: rispettare spessori minimi e distanze minime tra nodi
- Preferire piastre rettangolari quando possibile

## 5) ID
- Se assegni tu gli ID, devono essere univoci
- Se è disponibile la generazione automatica degli ID, preferirla per ridurre collisioni

## 6) Privacy & sicurezza
- Non includere dati o modelli reali di clienti
- Se devi mostrare un caso, usa geometrie sintetiche e anonimizzate
