# ============================================================
# MasterSap Script
# Titolo: Esempio01
# Autore: AG - AMV
# Licenza: Apache-2.0
# Testato su: MasterSap 2026 R1
# Unità: <kg; cm>
# Scopo: Esempio applicativo
# Input: no
# Output: Edificio a 2 piani in c.a.
# Limitazioni: Esempio d’uso
# ============================================================

import MS
MS.SetUndo()

# Materiali
mat_c4050 = MS.SetMaterial("C40/50")
mat_c7085 = MS.SetMaterial("C70/85")
mat_acciaio = MS.SetMaterial("Acciaio")

# Sezioni
MS.Section(1, 2, "Rp", 50.0, 50.0)
MS.Section(2, 2, "Rp", 30.0, 50.0)
MS.Section(3, 1, "HEA 300")

# Gruppi
MS.DefineGroup(1, "PIASTRA", "Piastre di platea")
MS.DefineGroup(1, "TRAVE", "Colonne piano 1 in calcestruzzo")
MS.DefineGroup(2, "TRAVE", "Travi piano 1 in calcestruzzo")
MS.DefineGroup(3, "TRAVE", "Colonne piano 2 in calcestruzzo")
MS.DefineGroup(4, "TRAVE", "Travi piano 2 in calcestruzzo")
MS.DefineGroup(5, "TRAVE", "Colonne piano 3 in acciaio")
MS.DefineGroup(6, "TRAVE", "Travi piano 3 in acciaio")

node_id = 1
beam_id = 1
plate_id = 1
nodes = {}


def get_node(x, y, z):
    global node_id
    key = (float(x), float(y), float(z))
    if key not in nodes:
        nodes[key] = node_id
        MS.Node(node_id, float(x), float(y), float(z))
        node_id += 1
    return nodes[key]


# Coordinate in cm
x_cols = [0.0, 260.0, 520.0, 780.0, 1040.0, 1300.0]
y_cols = [0.0, 200.0, 400.0, 600.0, 800.0]
z_levels = [0.0, 350.0, 700.0, 1050.0]

# Platea almeno 1 m oltre la pianta in ogni direzione.
# La maglia delle piastre e costruita in modo che i nodi di base dei pilastri
# coincidano con nodi delle piastre e che ogni piastra abbia lato <= 70 cm.
x_plate = [
    -100.0, -50.0, 0.0,
    65.0, 130.0, 195.0, 260.0,
    325.0, 390.0, 455.0, 520.0,
    585.0, 650.0, 715.0, 780.0,
    845.0, 910.0, 975.0, 1040.0,
    1105.0, 1170.0, 1235.0, 1300.0,
    1350.0, 1400.0,
]
y_plate = [
    -100.0, -50.0, 0.0, 50.0, 100.0, 150.0, 200.0, 250.0, 300.0, 350.0,
    400.0, 450.0, 500.0, 550.0, 600.0, 650.0, 700.0, 750.0, 800.0, 850.0,
    900.0,
]


# Nodi della maglia strutturale ai diversi livelli.
for z in z_levels:
    for x in x_cols:
        for y in y_cols:
            get_node(x, y, z)

# Nodi della platea sul piano z = 0.
for x in x_plate:
    for y in y_plate:
        get_node(x, y, 0.0)


# Platea in piastre di spessore 50 cm.
MS.ActivateGroup(1)
for ix in range(len(x_plate) - 1):
    for iy in range(len(y_plate) - 1):
        n1 = get_node(x_plate[ix], y_plate[iy], 0.0)
        n2 = get_node(x_plate[ix + 1], y_plate[iy], 0.0)
        n3 = get_node(x_plate[ix + 1], y_plate[iy + 1], 0.0)
        n4 = get_node(x_plate[ix], y_plate[iy + 1], 0.0)
        MS.Plate(plate_id, mat_c7085, 50.0, n1, n2, n3, n4)
        plate_id += 1


# Colonne piano 1 in calcestruzzo: da z = 0 a z = 350 cm.
MS.ActivateGroup(1)
for x in x_cols:
    for y in y_cols:
        n1 = get_node(x, y, 0.0)
        n2 = get_node(x, y, 350.0)
        MS.Beam(beam_id, mat_c4050, 1, n1, n2)
        beam_id += 1


# Travi piano 1 in calcestruzzo al livello z = 350 cm.
MS.ActivateGroup(2)
for y in y_cols:
    for ix in range(len(x_cols) - 1):
        n1 = get_node(x_cols[ix], y, 350.0)
        n2 = get_node(x_cols[ix + 1], y, 350.0)
        MS.Beam(beam_id, mat_c4050, 2, n1, n2)
        beam_id += 1
for x in x_cols:
    for iy in range(len(y_cols) - 1):
        n1 = get_node(x, y_cols[iy], 350.0)
        n2 = get_node(x, y_cols[iy + 1], 350.0)
        MS.Beam(beam_id, mat_c4050, 2, n1, n2)
        beam_id += 1


# Colonne piano 2 in calcestruzzo: da z = 350 a z = 700 cm.
MS.ActivateGroup(3)
for x in x_cols:
    for y in y_cols:
        n1 = get_node(x, y, 350.0)
        n2 = get_node(x, y, 700.0)
        MS.Beam(beam_id, mat_c4050, 1, n1, n2)
        beam_id += 1


# Travi piano 2 in calcestruzzo al livello z = 700 cm.
MS.ActivateGroup(4)
for y in y_cols:
    for ix in range(len(x_cols) - 1):
        n1 = get_node(x_cols[ix], y, 700.0)
        n2 = get_node(x_cols[ix + 1], y, 700.0)
        MS.Beam(beam_id, mat_c4050, 2, n1, n2)
        beam_id += 1
for x in x_cols:
    for iy in range(len(y_cols) - 1):
        n1 = get_node(x, y_cols[iy], 700.0)
        n2 = get_node(x, y_cols[iy + 1], 700.0)
        MS.Beam(beam_id, mat_c4050, 2, n1, n2)
        beam_id += 1


# Colonne piano 3 in acciaio HEA: da z = 700 a z = 1050 cm.
MS.ActivateGroup(5)
for x in x_cols:
    for y in y_cols:
        n1 = get_node(x, y, 700.0)
        n2 = get_node(x, y, 1050.0)
        MS.Beam(beam_id, mat_acciaio, 3, n1, n2)
        beam_id += 1


# Travi piano 3 in acciaio HEA al livello z = 1050 cm.
MS.ActivateGroup(6)
for y in y_cols:
    for ix in range(len(x_cols) - 1):
        n1 = get_node(x_cols[ix], y, 1050.0)
        n2 = get_node(x_cols[ix + 1], y, 1050.0)
        MS.Beam(beam_id, mat_acciaio, 3, n1, n2)
        beam_id += 1
for x in x_cols:
    for iy in range(len(y_cols) - 1):
        n1 = get_node(x, y_cols[iy], 1050.0)
        n2 = get_node(x, y_cols[iy + 1], 1050.0)
        MS.Beam(beam_id, mat_acciaio, 3, n1, n2)
        beam_id += 1

MS.Redraw()
