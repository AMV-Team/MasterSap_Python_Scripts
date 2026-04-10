# MasterPy commands

> Converted from the original Word document **MasterPy commands - Rev. 26.04**.

MasterPy commands

Guida agli script Python® MS

Riferimento rapido per utenti MasterSap.

# Introduzione

MasterSap (abbreviato MS) è un programma di calcolo strutturale che supporta la modellazione tramite script Python®. Questi script permettono di generare automaticamente costruzioni tridimensionali composte da travi, colonne e piastre, riducendo i tempi di input e rendendo il modello facilmente parametrico e riproducibile.

Si utilizza l’ambiente MasterPy per il supporto di script in linguaggio Python® arricchiti con comandi specifici per MasterSap inseriti in una libreria detta MS.

Essa viene importata automaticamente dall'ambiente di esecuzione MasterPy che è una console. Gli script devono contenere solo caratteri ASCII, i comandi sono ‘case sensitive’ quindi bisogna prestare attenzione ad inserire le lettere maiuscole e minuscole, cioè rispettare la sintassi dei comandi descritti in questa guida.

Per conoscere i fondamenti del linguaggio Python® si può fare riferimento al seguente link: www.python.org ed esplorare la documentazione disponibile.

Per avviare con successo uno script che venga quindi recepito in MasterSap o per inviare manualmente un comando MS, tramite l’ambiente a console MasterPy, il programma MasterSap deve essere in esecuzione con un progetto vuoto aperto.

## Concetti fondamentali

Nodi: punti nello spazio 3D che collegano gli elementi strutturali. Ogni nodo ha un identificativo univoco (nodeID) e coordinate X, Y, Z.

Travi e Colonne: elementi monodimensionali che collegano due nodi. Le colonne sono travi disposte verticalmente. Ogni elemento ha un identificativo univoco (beamID).

Piastre: elementi bidimensionali triangolari o quadrilateri che collegano 3 o 4 nodi. Si usano per modellare pareti, platee, cupole e superfici curve. Ogni piastra ha un identificativo univoco (plateID).

Macro: elemento simile alla piastra ma di grandi dimensioni che MasterSap suddivide autonomamente in piastre più piccole.

Gruppi: contenitori logici per gli elementi (travi o piastre). Ogni elemento deve appartenere a un gruppo attivo. I gruppi servono di solito a identificare i piani di un edificio.

## Unità di misura

Prima di generare qualsiasi elemento occorre stabilire l'unità di misura dello script: cm (centimetri) oppure m (metri). Tutte le coordinate, lunghezze e spessori devono essere espressi nell’unità scelta; se si propende per i comandi in cm e poi si inseriscono dati in m quei dati saranno interpretati in cm.

## Struttura tipica di uno script

Uno script MasterSap completo segue tipicamente questo schema:

import MS

# 1. Imposta il punto di undo

MS.SetUndo()

# 2. Definizione dei materiali

matID = MS.SetMaterial('C25/30')

# 3. Definizione delle sezioni

MS.Section(1, 2, 'Rp', 30.0, 50.0)

# 4. Definizione dei nodi

n1 = MS.Node(0, 0.0, 0.0, 0.0)

n2 = MS.Node(0, 500.0, 0.0, 0.0)

# 5. Creazione gruppi ed elementi

MS.DefineGroup(1, 'TRAVE', 'Travi piano terra')

MS.ActivateGroup(1, 'TRAVE')

MS.Beam(0, matID, 1, n1, n2)

# 6. Ridisegno finale

MS.Redraw()

# Comandi MS

Di seguito sono descritti tutti i comandi MS specifici di MasterSap. Si assume che il modulo MS sia già stato importato.

Prestare attenzione a maiuscole e minuscole perché il Python® è un linguaggio case sensitive così come i comandi MS.

I valori numerici float vanno scritti sempre con il punto decimale (es. 30.0, non 30). I numeri interi si scrivono senza il punto decimale (es. 30). Le stringhe devono essere racchiuse tra ' (apici) o tra " (virgolette), p.es: 'C8/10' oppure "C8/10".

### MS.SetMaterial

Definisce un materiale nella banca locale del progetto e restituisce il suo identificativo numerico (materialID), da usare poi nei comandi MS.Beam e MS.Plate.

Sintassi:

materialID = MS.SetMaterial(materialName)

Parametri:

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| materialName | stringa | Nome del materiale. Valori accettati elencati di seguito. |

Valori accettati per materialName:

# Calcestruzzo / cemento armato

# 'C8/10','C12/15','C16/20','C20/25','C25/30','C28/35',

# 'C30/37','C32/40','C35/45','C40/50','C45/55','C50/60'

# 'C55/67','C60/75','C70/85','C80/95','C90/105'

# Altri materiali

# 'Acciaio','Legno','Muratura','Alluminio','Ghisa','Vetro'

Valore restituito: intero – identificativo del materiale (materialID).

Esempio:

matCA  = MS.SetMaterial('C25/30')

matAcc = MS.SetMaterial('Acciaio')

matMur = MS.SetMaterial('Muratura')

### MS.Section

Definisce una sezione trasversale per le travi, identificata da un sectionID progressivo. Esistono due tipologie: profili a caldo UNI in acciaio (sectionType = 1) e sezioni ricorrenti parametriche di qualunque materiale (sectionType = 2).

Nota: non usare MS.Section per le piastre. Lo spessore delle piastre si definisce direttamente in MS.Plate.

Sintassi:

# Profilo a caldo UNI (sectionType = 1)

MS.Section(sectionID, 1, sectionName)

# Sezione ricorrente parametrica (sectionType = 2)

MS.Section(sectionID, 2, sectionName, param1, param2, ...)

Parametri:

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| sectionID | intero | Identificativo univoco della sezione, progressivo da 1. |
| sectionType | intero | 1 = profilo a caldo UNI in acciaio; 2 = sezione ricorrente parametrica. |
| sectionName | stringa | Per sectionType=1: sigla profilo, es. 'HEA 200', 'IPE 300', 'L 100x10'. Per sectionType=2: 'Rp', 'Cp', 'Rf', 'Cc'. |
| param1, ... | float | Per sectionType=2: dimensioni geometriche della sezione |

Sezioni ricorrenti disponibili (sectionType = 2):

| sectionName | Tipo sezione | Descrizione |
| --- | --- | --- |
| Rp | Rettangolare piena | param1 = base, param2 = altezza |
| Cp | Circolare piena | param1 = diametro |
| Rf | Rettangolare cava | param1 = base, param2 = altezza, param3 = spessore orizzontale, param4 = spessore verticale |
| Cc | Circolare cava | param1 = diametro, param2 = spessore |

Profili a caldo UNI (sectionType = 1):

In section name si mettono le sigle seguite dalla dimensione: HEA, HEB, HEM, HLS, IPE, ILS, IPN, UNP, L. La dimensione è sempre in mm.

Es. 'HEA 200', 'IPE 300'. Per i profili ad L: 'L 100x10' (lati uguali) oppure 'L 100x50x6' (lati diversi).

Valore restituito: nessuno.

Esempio:

MS.Section(1, 2, 'Rp', 30.0, 50.0)           # rettangolare piena 30x50 cm

MS.Section(2, 2, 'Cp', 40.0)                 # circolare piena diam. 40 cm

MS.Section(3, 2, 'Rf', 20.0, 30.0, 2.0, 2.0) # rettangolare cava

MS.Section(4, 1, 'HEA 200')                  # profilo HEA 200

MS.Section(5, 1, 'IPE 300')                  # profilo IPE 300

MS.Section(6, 1, 'L 100x10')                 # angolare L 100x10

### MS.Node

Definisce un nodo nello spazio tridimensionale. Il nodeID puo' essere assegnato manualmente (da 1 in poi) oppure lasciato a MasterSap (mettendo nodeID = 0); in quest'ultimo caso il valore restituito va salvato in una variabile per poterlo riutilizzare negli altri comandi.

Nota: se si usa nodeID = 0 per un nodo, usare 0 per tutti i nodi dello script e non mischiare i due approcci.

Sintassi:

nodeID_ret = MS.Node(nodeID, coordinataX, coordinataY, coordinataZ)

Parametri:

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| nodeID | intero | 0 = MasterSap assegna automaticamente il nodo. Altrimenti: intero progressivo da 1, univoco nel progetto. |
| coordinataX | float | Coordinata X del nodo nell'unità di misura corrente. |
| coordinataY | float | Coordinata Y del nodo nell'unità di misura corrente. |
| coordinataZ | float | Coordinata Z del nodo nell'unità di misura corrente. |

Valore restituito: intero – l'identificativo del nodo (generato da MasterSap se nodeID = 0, altrimenti uguale al nodeID passato nei parametri).

Esempio con nodeID automatico:

n1 = MS.Node(0, 0.0, 0.0, 0.0)   # origine

n2 = MS.Node(0, 500.0, 0.0, 0.0)

n3 = MS.Node(0, 500.0, 500.0, 0.0)

n4 = MS.Node(0, 0.0, 500.0, 0.0)

n5 = MS.Node(0, 0.0, 0.0, 300.0) # piano superiore

Esempio con nodeID manuale:

MS.Node(1, 0.0, 0.0, 0.0)

MS.Node(2, 500.0, 0.0, 0.0)

MS.Node(3, 500.0, 500.0, 0.0)

### MS.DefineGroup

Definisce un nuovo gruppo di elementi. I gruppi TRAVE e PIASTRA hanno sequenze di numerazione indipendenti, entrambe a partire da 1 senza buchi. Un gruppo può contenere al massimo 1999 elementi.

Sintassi:

MS.DefineGroup(groupID, groupType, groupName)

Parametri:

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| groupID | intero | Identificativo del gruppo. Progressivo da 1, indipendente per ciascun groupType. Non sono ammessi buchi di numerazione. |
| groupType | stringa | 'TRAVE' per gruppi di travi/colonne; 'PIASTRA' per gruppi di piastre o macro. |
| groupName | stringa | Nome descrittivo del gruppo (es. 'Travi primo piano', 'Colonne piano terra', 'Piastre di platea'). |

Valore restituito: nessuno.

Esempio:

# Gruppi di travi (numerazione indipendente da 1)

MS.DefineGroup(1, 'TRAVE', 'Colonne piano terra')

MS.DefineGroup(2, 'TRAVE', 'Travi piano primo')

# Gruppi di piastre (numerazione separata, riparte da 1)

MS.DefineGroup(1, 'PIASTRA', 'Pareti piano terra')

MS.DefineGroup(2, 'PIASTRA', 'Platea di fondazione')

### MS.ActivateGroup

Attiva il gruppo specificato. Tutti gli elementi creati dopo questa chiamata (tramite MS.Beam o MS.Plate) verranno aggiunti al gruppo attivo, fino a quando non viene attivato un nuovo gruppo.

Sintassi:

MS.ActivateGroup(groupID, groupType)

Parametri:

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| groupID | intero | Identificativo del gruppo da attivare. |
| groupType | stringa | 'TRAVE' o 'PIASTRA'. Parametro opzionale: se omesso si assume 'TRAVE'. |

Valore restituito: nessuno.

Esempio:

MS.ActivateGroup(1, 'TRAVE')

MS.Beam(0, matID, 1, n1, n5)   # va nel gruppo 1 TRAVE

MS.Beam(0, matID, 1, n2, n6)   # va nel gruppo 1 TRAVE

MS.ActivateGroup(2, 'TRAVE')

MS.Beam(0, matID, 2, n5, n6)   # va nel gruppo 2 TRAVE

MS.ActivateGroup(1, 'PIASTRA')

MS.Plate(0, matID, 20.0, n1, n2, n3, n4)  # va nel gruppo 1 PIASTRA

### MS.Beam

Genera una trave che collega due nodi. L'elemento richiede un materiale, una sezione e deve essere creato con un gruppo attivo.

Sintassi:

beamID_ret = MS.Beam(beamID, materialID, sectionID, nodeI, nodeJ)

Parametri:

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| beamID | intero | 0 = MasterSap assegna automaticamente (consigliato). Altrimenti: intero da 1, univoco tra tutti gli elementi del progetto (travi e piastre). |
| materialID | intero | Identificativo del materiale, ottenuto da MS.SetMaterial(). |
| sectionID | intero | Identificativo della sezione, definita con MS.Section(). |
| nodeI | intero | Identificativo del nodo iniziale (estremo I). |
| nodeJ | intero | Identificativo del nodo finale (estremo J). |

Valore restituito: intero – identificativo dell'elemento generato.

Esempio – telaio con colonne e trave:

matID = MS.SetMaterial('C25/30')

MS.Section(1, 2, 'Rp', 30.0, 30.0)   # colonne 30x30 cm

MS.Section(2, 2, 'Rp', 30.0, 50.0)   # travi 30x50 cm

n1 = MS.Node(0, 0.0, 0.0, 0.0)

n2 = MS.Node(0, 400.0, 0.0, 0.0)

n3 = MS.Node(0, 0.0, 0.0, 300.0)

n4 = MS.Node(0, 400.0, 0.0, 300.0)

MS.DefineGroup(1, 'TRAVE', 'Colonne')

MS.ActivateGroup(1, 'TRAVE')

MS.Beam(0, matID, 1, n1, n3)   # colonna sinistra

MS.Beam(0, matID, 1, n2, n4)   # colonna destra

MS.DefineGroup(2, 'TRAVE', 'Travi')

MS.ActivateGroup(2, 'TRAVE')

MS.Beam(0, matID, 2, n3, n4)   # trave orizzontale

### MS.Plate

Genera una piastra triangolare o quadrilatero planare. Si usa per modellare pareti, platee, cupole e superfici curve. Piastre adiacenti devono condividere i nodi sul bordo comune. La normale alla piastra segue la regola della mano destra nell'ordine nodeI -> nodeJ -> nodeK (-> nodeL).

Sintassi:

# Quadrilatero (4 nodi)

plateID_ret = MS.Plate(plateID, materialID, spess, nodeI, nodeJ, nodeK, nodeL)

# Triangolo (3 nodi)

plateID_ret = MS.Plate(plateID, materialID, spess, nodeI, nodeJ, nodeK)

Parametri:

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| plateID | intero | 0 = MasterSap assegna automaticamente (consigliato). Altrimenti: intero da 1, univoco tra tutti gli elementi del progetto. |
| materialID | intero | Identificativo del materiale, ottenuto da MS.SetMaterial. |
| spess | float | Spessore della piastra nell'unita' di misura corrente (minimo 1 cm). |
| nodeI | intero | Primo nodo. |
| nodeJ | intero | Secondo nodo. |
| nodeK | intero | Terzo nodo. |
| nodeL | intero | Quarto nodo (solo per quadrilateri, opzionale). |

Valore restituito: intero – identificativo della piastra generata.

Esempio – parete rettangolare 400x300 cm, spessore 20 cm:

matID = MS.SetMaterial('C25/30')

p1 = MS.Node(0, 0.0, 0.0, 0.0)

p2 = MS.Node(0, 400.0, 0.0, 0.0)

p3 = MS.Node(0, 400.0, 0.0, 300.0)

p4 = MS.Node(0, 0.0, 0.0, 300.0)

MS.DefineGroup(1, 'PIASTRA', 'Parete')

MS.ActivateGroup(1, 'PIASTRA')

MS.Plate(0, matID, 20.0, p1, p2, p3, p4)

Esempio – parete suddivisa in mesh 2x2:

n = {}

for iz, z in enumerate([0.0, 150.0, 300.0]):

    for ix, x in enumerate([0.0, 200.0, 400.0]):

        n[(ix, iz)] = MS.Node(0, x, 0.0, z)

MS.DefineGroup(1, 'PIASTRA', 'Parete mesh')

MS.ActivateGroup(1, 'PIASTRA')

for iz in range(2):

    for ix in range(2):

        MS.Plate(0, matID, 20.0,

                 n[(ix, iz)],

                 n[(ix+1, iz)],

                 n[(ix+1, iz+1)],

                 n[(ix, iz+1)])

### MS.Macro

Genera una macro, ovvero un elemento bidimensionale di grandi dimensioni che MasterSap suddivide internamente in piastre più piccole. Si usa principalmente per platee o per coprire superfici piane ampie (lati tipicamente superiori a 100 cm). A differenza delle piastre, la macro non viene mai suddivisa dallo script.

Importante: ogni macro deve essere inserita in un gruppo PIASTRA dedicato esclusivamente a lei (senza altri elementi).

Sintassi:

# Quadrilatero (4 nodi)

MS.Macro(macroName, materialID, spess, nodeI, nodeJ, nodeK, nodeL)

# Triangolo (3 nodi)

MS.Macro(macroName, materialID, spess, nodeI, nodeJ, nodeK)

Parametri:

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| macroName | stringa | Nome della macro (max 50 caratteri ASCII). Es. 'Platea fondazione', 'Solaio piano terra'. |
| materialID | intero | Identificativo del materiale, ottenuto da MS.SetMaterial. |
| spess | float | Spessore della macro nell'unita' di misura corrente. |
| nodeI..L | intero | Identificativi dei nodi ai vertici (3 per triangolo, 4 per quadrilatero). |

Valore restituito: nessuno.

Esempio – platea di fondazione 10x8 m, spessore 60 cm (misure in cm):

matID = MS.SetMaterial('C25/30')

p1 = MS.Node(0, 0.0, 0.0, 0.0)

p2 = MS.Node(0, 1000.0, 0.0, 0.0)

p3 = MS.Node(0, 1000.0, 800.0, 0.0)

p4 = MS.Node(0, 0.0, 800.0, 0.0)

# Gruppo dedicato esclusivamente alla macro

MS.DefineGroup(1, 'PIASTRA', 'Macro platea')

MS.ActivateGroup(1, 'PIASTRA')

MS.Macro('Platea fondazione', matID, 60.0, p1, p2, p3, p4)

### MS.SetUndo

Fissa un punto di ripristino prima della generazione del modello. In caso di necessità di ripartire, il programma potrà tornare a questo stato. Va inserito una sola volta all'inizio dello script.

Sintassi:

MS.SetUndo()

Parametri: nessuno.

Valore restituito: nessuno.

Esempio:

MS.SetUndo()

# ... generazione del modello ...

### MS.Redraw

Ridisegna la scena in MasterSap, aggiornando la visualizzazione 3D del modello. Va chiamato una sola volta come ultima istruzione dello script.

Sintassi:

MS.Redraw()

Parametri: nessuno.

Valore restituito: nessuno.

Esempio:

# ... generazione nodi, sezioni, travi ...

MS.Redraw()   # ultima riga dello script

# Avviamento di uno script MasterSap nella console MasterPy

Si ricorda che per avviare con successo uno script MasterSap (o per inviare manualmente un comando MS), il programma MasterSap deve essere in esecuzione con un progetto vuoto aperto.

### go

Comando semplificato per avviare uno script MasterSap.

Sintassi:

go(nomefile)

Parametri:

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| nomefile | stringa | nome dello script con estensione .py da eseguire. Questo script si deve trovare nella cartella Documenti dell’utente o nella cartella Donwload di default del sistema Windows |

Esempio:

go('myscript.py') #solo con myscript.py nella cartella Documenti dell’utente

Note:

Questo comando specifico di MasterPy è stato inserito per semplificare l’avvio di uno script che si trovi nella cartella Documenti dell’utente o nella cartella Download di defautl del sistema Windows.

L’avvio di uno script “myscript.py” si può sempre ottenere tramite il comando standard di Python, specificando un percorso generico:

 exec(open("C:/Users/utente/Documents/myscript.py").read())

Se il file “myscript.py” viene messo nella cartella documenti dell’utente, in modo più semplificato, grazie alla console di MasterPy, si può fare:

go('myscript.py')

# Esempio: edificio a due piani

Lo script seguente genera un edificio a due piani con quattro colonne, travi perimetrali e macro di solaio. L'unità di misura è il centimetro. La pianta è 500x500 cm, i piani sono alti 300 cm ciascuno.

import MS

MS.SetUndo()

# Materiali

matCA = MS.SetMaterial('C25/30')

# Sezioni

MS.Section(1, 2, 'Rp', 40.0, 40.0)   # colonne 40x40 cm

MS.Section(2, 2, 'Rp', 30.0, 60.0)   # travi 30x60 cm

# Nodi a terra (Z=0)

n1 = MS.Node(0, 0.0, 0.0, 0.0)

n2 = MS.Node(0, 500.0, 0.0, 0.0)

n3 = MS.Node(0, 500.0, 500.0, 0.0)

n4 = MS.Node(0, 0.0, 500.0, 0.0)

# Nodi piano 1 (Z=300)

n5 = MS.Node(0, 0.0, 0.0, 300.0)

n6 = MS.Node(0, 500.0, 0.0, 300.0)

n7 = MS.Node(0, 500.0, 500.0, 300.0)

n8 = MS.Node(0, 0.0, 500.0, 300.0)

# Nodi piano 2 (Z=600)

n9 = MS.Node(0, 0.0, 0.0, 600.0)

n10 = MS.Node(0, 500.0, 0.0, 600.0)

n11 = MS.Node(0, 500.0, 500.0, 600.0)

n12 = MS.Node(0, 0.0, 500.0, 600.0)

# Colonne piano terra

MS.DefineGroup(1, 'TRAVE', 'Colonne piano terra')

MS.ActivateGroup(1, 'TRAVE')

for base, top in [(n1,n5),(n2,n6),(n3,n7),(n4,n8)]:

    MS.Beam(0, matCA, 1, base, top)

# Colonne piano primo

MS.DefineGroup(2, 'TRAVE', 'Colonne piano primo')

MS.ActivateGroup(2, 'TRAVE')

for base, top in [(n5,n9),(n6,n10),(n7,n11),(n8,n12)]:

    MS.Beam(0, matCA, 1, base, top)

# Travi piano primo

MS.DefineGroup(3, 'TRAVE', 'Travi piano primo')

MS.ActivateGroup(3, 'TRAVE')

for ni, nj in [(n5,n6),(n6,n7),(n7,n8),(n8,n5)]:

    MS.Beam(0, matCA, 2, ni, nj)

# Travi piano secondo

MS.DefineGroup(4, 'TRAVE', 'Travi piano secondo')

MS.ActivateGroup(4, 'TRAVE')

for ni, nj in [(n9,n10),(n10,n11),(n11,n12),(n12,n9)]:

    MS.Beam(0, matCA, 2, ni, nj)

# Solaio piano primo

MS.DefineGroup(1, 'PIASTRA', 'Solaio piano primo')

MS.ActivateGroup(1, 'PIASTRA')

MS.Macro('Solaio1', matCA, 20.0, n5, n6, n7, n8)

# Solaio piano secondo

MS.DefineGroup(2, 'PIASTRA', 'Solaio piano secondo')

MS.ActivateGroup(2, 'PIASTRA')

MS.Macro('Solaio2', matCA, 20.0, n9, n10, n11, n12)

MS.Redraw()


## Images

![masterpy_image_1_e23234445be3.png](docs/assets/masterpy_image_1_e23234445be3.png)

