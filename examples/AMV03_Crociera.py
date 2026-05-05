# ============================================================
# MasterSap Script
# Titolo: Esempio03
# Autore: AG - AMV
# Licenza: Apache-2.0
# Testato su: MasterSap 2026 R1
# Unità: <kg; cm>
# Scopo: Esempio applicativo
# Input: Raggio, lato, passo
# Output: Volta a crociera su impianto quadrato (solo nodi)
# Limitazioni: Esempio d’uso
# ============================================================

import math
import MS

MS.SetUndo()

# Unita in cm
R = 500.0
LATO = 1500.0
PASSO_ANG = 10.0

# Volta a crociera su impianto quadrato LATO x LATO.
# Si generano i nodi dei 4 archi di imposta a tutto sesto
# e i nodi di intersezione tra:
# - le rette che uniscono punti corrispondenti degli archi nord-sud
# - le rette che uniscono punti corrispondenti degli archi est-ovest

node_id = 1
node_map = {}


def add_node(x, y, z):
    global node_id
    key = (round(x, 6), round(y, 6), round(z, 6))
    if key not in node_map:
        MS.Node(node_id, float(x), float(y), float(z))
        node_map[key] = node_id
        node_id += 1
    return node_map[key]


def rounded(value):
    return round(value, 6)


# Archi est-ovest: lati AB e CD
# Archi nord-sud: lati BC e DA
arc_ab = []
arc_bc = []
arc_cd = []
arc_da = []

# Arco lato AB: piano y = -LATO/2, sviluppo su x
ang = 180.0
while ang >= 0.0:
    rad = math.radians(ang)
    x = R * math.cos(rad)
    y = -LATO / 2.0
    z = R * math.sin(rad)
    add_node(x, y, z)
    arc_ab.append((x, y, z))
    ang -= PASSO_ANG

# Arco lato BC: piano x = LATO/2, sviluppo su y
ang = 180.0
while ang >= 0.0:
    rad = math.radians(ang)
    x = LATO / 2.0
    y = R * math.cos(rad)
    z = R * math.sin(rad)
    add_node(x, y, z)
    arc_bc.append((x, y, z))
    ang -= PASSO_ANG

# Arco lato CD: piano y = LATO/2, sviluppo su x
ang = 180.0
while ang >= 0.0:
    rad = math.radians(ang)
    x = -R * math.cos(rad)
    y = LATO / 2.0
    z = R * math.sin(rad)
    add_node(x, y, z)
    arc_cd.append((x, y, z))
    ang -= PASSO_ANG

# Arco lato DA: piano x = -LATO/2, sviluppo su y
ang = 180.0
while ang >= 0.0:
    rad = math.radians(ang)
    x = -LATO / 2.0
    y = -R * math.cos(rad)
    z = R * math.sin(rad)
    add_node(x, y, z)
    arc_da.append((x, y, z))
    ang -= PASSO_ANG

# Per ogni quota z si raccolgono:
# - i valori x dei punti corrispondenti sugli archi est-ovest AB/CD
# - i valori y dei punti corrispondenti sugli archi nord-sud BC/DA
# Ogni intersezione tra queste due famiglie di rette genera un nuovo nodo.
xs_by_z = {}
ys_by_z = {}

for x, y, z in arc_ab:
    z_key = rounded(z)
    if z_key not in xs_by_z:
        xs_by_z[z_key] = set()
    xs_by_z[z_key].add(rounded(x))

for x, y, z in arc_cd:
    z_key = rounded(z)
    if z_key not in xs_by_z:
        xs_by_z[z_key] = set()
    xs_by_z[z_key].add(rounded(x))

for x, y, z in arc_bc:
    z_key = rounded(z)
    if z_key not in ys_by_z:
        ys_by_z[z_key] = set()
    ys_by_z[z_key].add(rounded(y))

for x, y, z in arc_da:
    z_key = rounded(z)
    if z_key not in ys_by_z:
        ys_by_z[z_key] = set()
    ys_by_z[z_key].add(rounded(y))

for z_key in sorted(xs_by_z.keys()):
    if z_key not in ys_by_z:
        continue
    xs = sorted(xs_by_z[z_key])
    ys = sorted(ys_by_z[z_key])
    for x_val in xs:
        for y_val in ys:
            add_node(x_val, y_val, z_key)

MS.Redraw()
