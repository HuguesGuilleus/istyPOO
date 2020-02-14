#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# GUILLEUS Hugues IATIC3 <hugues.guilleus@ens.uvsq.fr>

import math


def question(nb):
	"Affiche le numéro de la question"
	print(f"\n\033[01;34m==== QUESTION: {nb}\033[0m")


def inputFloat(prompt):
	"""
	inputFloat retourne un flotant saisit par l'utilisteur. En de mauvaises entrés
	on redemande à l'utilisateur le flottant.
	"""
	while True:
		try:
			f = float(input(prompt))
		except: pass
		else: return f


question(1)
f = inputFloat("flotant: ")
if f < 0:
	print(f"Le flotant {f} est négatif")
else:
	print(f"racine de {f}: {math.sqrt(f)}")


question(2)
print(f"Saisissez deux mots:")
m1=input("mot 1: ")
m2=input("mot 2: ")
if m1 < m2:
	print(f"'{m1}' est plus petit que '{m2}'")
else:
	print(f"'{m2}' est plus petit que '{m1}'")


question(3)
p = inputFloat("pression: ")
v = inputFloat("volume: ")
pSeuil = 2.3
vSeuil = 7.41
if p>pSeuil and v>vSeuil:
	print("arrêt immédiat")
elif p>pSeuil:
	print("Augmenter le volume de l'enceinte")
elif v>vSeuil:
	print("Diminuer le volume de l'enceinte")
else:
	print(f"Tout va bien")


question(4)
b = 10
for a in range(b):
	print(f"a: {a}")
print()
while b > 0:
	if b%2 : print(f"b: {b}")
	b -= 1


question(5)
for c in input("chaîne de caractère: "):
	print(f"c: '{c}'")


question(6)
for i in range(1, 15, 3):
	print(f"i: {i}")
