#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# GUILLEUS Hugues IATIC3 <hugues.guilleus@ens.uvsq.fr>

# Iterre sur le nombre de question
questionNum=0
def question(name=""):
	"Affiche le numéro de la question"
	global questionNum
	questionNum+=1
	if name:
		print(f"\n\033[01;44m==== QUESTION\033[0m \033[1;34m{questionNum}: {name}\033[0m\n")
	else:
		print(f"\n\033[01;44m==== QUESTION\033[0m \033[1;34m{questionNum}\033[0m\n")

question("Liste sans doublons")

def uniqSorted(tab):
	"""
	Supprime les doublons dans un tableau trié.
	"""
	if len(tab) == 0:
		return

	old = tab[-1]
	# Comme on modifie la liste en cours de route on ne peut pas faire une
	# itération classique.
	i = 0
	while i < len(tab):
		v = tab[i]
		# Comme python est faiblement typé on est obliger de tester aussi le
		# type
		if v == old and type(v) == type(old):
			tab.pop(i)
			continue
		old = v
		i += 1
l = [1,1,2,2,2,3,4,4]
print(f"l: {l}")
uniqSorted(l)
print(f"l: {l}")

def uniqNotSorted(tab):
	""""
	Supprime tous les éléments dans le tableau en doublon. Le tableau n'a pas
	besoin d'être trié.
	"""
	i = 0;
	while i < len(tab):
		v = tab[i]
		j = 0
		while j < len(tab[:i]):
			w = tab[j]
			if w == v and type(v) == type(w):
				print(f"on vire le doublon {v}")
				tab.pop(i)
				i -= 1 # pour ne pas ittérer le i
				break
			j += 1
		i += 1
l = [1, 2, 14, 3, 2, 2, 4, 4, 4, 4, 3, True, "yolo", "yolo"]
print(f"l: {l}")
uniqNotSorted(l)
print(f"l: {l}")


question("Liste plate")
def applattissment(src):
	list = []
	for l in src:
		list.extend(l)
	return list

print(applattissment([[1,2],[3,4]]))
