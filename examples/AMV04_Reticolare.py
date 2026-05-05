# ============================================================
# MasterSap Script
# Titolo: Esempio04
# Autore: AG - AMV
# Licenza: Apache-2.0
# Testato su: MasterSap 2026 R1
# Unità: <kg; m>
# Scopo: Esempio applicativo
# Input: Total span, half span, roof angle, initial height
# Output: Steel Mohnie truss with alternating diagonals
# Limitazioni: Esempio d’uso
# ============================================================

import math
MS.SetUndo()

# ------------------------------------------------------------
# Parameters
# ------------------------------------------------------------
total_span = 20.0
half_span = total_span / 2.0
roof_angle_deg = 10.0
roof_angle_rad = math.radians(roof_angle_deg)
initial_height = 1.0

# Six verticals for each roof slope, counting the ridge on both slopes.
# Unique x positions are therefore: 0, 2, 4, ..., 20
panel_x = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]

def top_z(x):
    if x <= half_span:
        return initial_height + math.tan(roof_angle_rad) * x
    return initial_height + math.tan(roof_angle_rad) * (total_span - x)

def fmt(v):
    return float(f"{v:.6f}")

# ------------------------------------------------------------
# Material and sections
# ------------------------------------------------------------
material_id = MS.SetMaterial("Acciaio")

# sectionID, sectionType, sectionName
MS.Section(1, 1, "L 110x10")
MS.Section(2, 1, "L 90x10")
MS.Section(3, 1, "L 80x8")
MS.Section(4, 1, "L 60x6")

section_top = 1
section_bottom = 2
section_vertical = 3
section_diagonal = 4

# ------------------------------------------------------------
# Groups
# ------------------------------------------------------------
MS.DefineGroup(1, "TRAVE", "Travatura reticolare Mohnie")
MS.ActivateGroup(1)

# ------------------------------------------------------------
# Nodes
# Bottom chord lies on Z = 0.0, Y = 0.0
# Top chord follows the two roof slopes
# ------------------------------------------------------------
bottom_nodes = []
top_nodes = []

node_id = 1

for x in panel_x:
    MS.Node(node_id, fmt(x), 0.0, 0.0)
    bottom_nodes.append(node_id)
    node_id += 1

for x in panel_x:
    MS.Node(node_id, fmt(x), 0.0, fmt(top_z(x)))
    top_nodes.append(node_id)
    node_id += 1

# ------------------------------------------------------------
# Beams
# ------------------------------------------------------------
beam_id = 1

def add_beam(section_id, node_i, node_j):
    global beam_id
    MS.Beam(beam_id, material_id, section_id, node_i, node_j)
    beam_id += 1

# Bottom chord
for i in range(len(bottom_nodes) - 1):
    add_beam(section_bottom, bottom_nodes[i], bottom_nodes[i + 1])

# Top chord
for i in range(len(top_nodes) - 1):
    add_beam(section_top, top_nodes[i], top_nodes[i + 1])

# Verticals
for i in range(len(panel_x)):
    add_beam(section_vertical, bottom_nodes[i], top_nodes[i])

# Alternating diagonals, one for each panel
# Even panel: from lower left to upper right
# Odd panel:  from upper left to lower right
for i in range(len(panel_x) - 1):
    if i % 2 == 0:
        add_beam(section_diagonal, bottom_nodes[i], top_nodes[i + 1])
    else:
        add_beam(section_diagonal, top_nodes[i], bottom_nodes[i + 1])

MS.Redraw()
