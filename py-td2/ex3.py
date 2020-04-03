#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# GUILLEUS Hugues IATIC3 <hugues.guilleus@ens.uvsq.fr>

import random

def des(j):
	"""
	Lance le dé tant que le joueur n'a pas gagné ou n'a pas fait 1.
	"""
	while True:
		input("Lancer le dé ")
		r = random.randint(1,6)

		if r == 1:
			print(f"On change de joueur")
			return j
		elif r == 3:
			j *= 2
		elif r == 5:
			j -= 2
		else:
			j += r

		if j >= 50:
			print(f"Le joueur courant à gagnez. FÉLICITAION!")
			return
		print(f"Le score du joueur courant: {j}")


# Les scores des deux joueurs.
u1, u2 = 0, 0
while u2 < 50:
	u1, u2 = u2, des(u1)
