# MasterSap Script
# Titolo: Edificio di 2 piani
# Autore: Giordano
# Licenza: Apache-2.0
# Testato su: MasterSap 2026
# Unità: cm
# Scopo: Esempio #1
# Input: nulla
# Output: genera un edificio elementare di 2 piani con quattro colonne, travi perimetrali e macro di solaio. La pianta e' 500x500 cm, i piani sono alti 300 cm ciascuno
# Limitazioni: Esempio d'uso

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

