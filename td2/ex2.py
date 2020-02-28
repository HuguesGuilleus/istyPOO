#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# GUILLEUS Hugues IATIC3 <hugues.guilleus@ens.uvsq.fr>

# Algorithme utilisé:
#	1. On génère aléatoirement un entier
#	2. On répète dix fois
#		2.1 On demande au joueur un nombre
#		2.2 Si le nombre donnée est égale on quitte le jeu
#		3.3 Sinon on indique si le nombre donnée est inférieur ou spérieur
#		au nombre généré.
#	3. Le joueur à perdu

import random

def inputInt(prompt, min=0, max=100):
	"""
	inputInt retourne un entier saisit par l'utilisteur. La saisit est
	sécurisée: en de mauvaises entrés on redemande à l'utilisateur l'entier.
	Si l'utilisateur quitte le proggrame avec Contrôle+C, le programme s'arrête.
	"""
	while True:
		try:
			i = int(input(prompt))
		except KeyboardInterrupt as e:
			print()
			exit(0)
		except Exception as e:
			print(f"Valeur invalide")
			continue
		if min <= i <= max:
			return i
		print(f"La valeur doit être entre ${min} et ${max}")

nbGen = random.randint(0,100)


for i in range(10):
	u = inputInt("entier> ", 0, 100)
	if u == nbGen:
		print(f"Vous avez gagné. FÉLICITATION!")
		break
	elif u < nbGen:
		print("Le nombre que vous avez rentré est trop petit")
	else:
		print("Le nombre qu vous avez rentré est trop grand")

print(f"Vous avez perdu le nombre était: {nbGen}")
