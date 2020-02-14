#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# GUILLEUS Hugues IATIC3 <hugues.guilleus@ens.uvsq.fr>

import re

# Récupération de l'entier positif
nb=-1
while nb < 0:
	inp = input("nb (entier positif): ")
	if re.match("\D",inp) != None: continue
	nb = int(inp)


# Algorithme1: on convertie en chaîne de caractère et on mesure sa longueur.
print("\nAlgo1: Chaîne de caractère")
l = len(str(nb))
print(f"  {nb} contient {l} digit")


# Méthode on divise par 10 tant que l'entier n'est pas null et on renvoie
# le nombre d'itération.
print("\nAlgo2: Division par 10")
n=nb
l=0
while n>0:
	n = int(n/10)
	l+=1
print(f"  {nb} contient {l} digit\n")


# Affichage des digits
unite = {
	0: "unités",
	1: "dizaines",
	2: "centaines",
	3: "milliers",
	6: "million",
	9: "milliard",
}
l=0
for n in str(nb)[::-1]:
	if l in unite:
		print(f"{n} {unite[l]}")
	else:
		print(f"{n} 10^{l}")
	l += 1
