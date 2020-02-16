#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# GUILLEUS Hugues IATIC3 <hugues.guilleus@ens.uvsq.fr>

couleur = {
	"r": "Rouge",
	"v": "Vert",
	"b": "bleu", # Je ne sais pas pourquoi le bleu est en minuscule.
}

inp = input("[rvb]: ").lower()
if inp in couleur:
	print(couleur[inp])
else:
	print("Couleur non reconnue")
