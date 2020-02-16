#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# GUILLEUS Hugues IATIC3 <hugues.guilleus@ens.uvsq.fr>

print("=== Première partie")
temps = 6.892
dist = 19.7
vit = dist / temps
print(f"vitesse: {vit}")
print("vitesse {0:.1f}".format(vit))

print("\n=== Deuxième partie")
nom = input("nom? ")
age = int(input("âge? "))
print(f"Vous êtes: {nom} et vous avez {age} ans.")

print("la fonction raw_input n'existe pas dans python3")
