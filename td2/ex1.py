#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# GUILLEUS Hugues IATIC3 <hugues.guilleus@ens.uvsq.fr>

import math

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


question("Valeurs consécutives")
def valConsecutives(list):
	if len(list) == 0:
		return []
	out = []
	before = list[0]
	for e in list[1:]:
		if before+1 == e:
			out.append((before, e))
		before = e
	return out
print(valConsecutives([3, 8, 9, 10, 15, 16]))


question("?")
def q4(d):
	c = 0
	number = type(0)
	for v in applattissment(d.values()):
			if type(v) == number:
				c += 1
	return c

print(q4({
	"a": [1, True, 5],
	"b": [False, 19, 8585],
}))


question("Des")
table = {}
for des1 in range(1,6):
	for des2 in range(1,6):
		table[des1+des2] = (des1, des2)
print(f"table: {table}")


question("Crible d'Eratosthène")
def nbFirst(n):
	if type(n) != type(0) and n < 2:
		raise "pas un nombre"
	max = int(math.sqrt(n))+1
	first = list(range(2, max))
	for i in first:
		if n%i != 0:
			for s in range(i, max+1, i):
				if s in first: first.remove(s)
		else:
			for s in range(i*2, max+1, i):
				if s in first: first.remove(s)
	return first
print(nbFirst(60))


question("Inversion")
def inversion(table):
	for i, v in table.copy().items():
		table.pop(i)
		table[v] = i
	return

t = {
	'a': True,
	'b': False,
}
inversion(t)
print(t)


question("Même lettres")
def sameLetter(word1, word2):
	for c in word1:
		if c not in word2:
			return False
	for c in word2:
		if c not in word1:
			return False
	return True
print(f'sameLetter("chinnnnne", "chien"): {sameLetter("chinnnnne", "chien")}')

def anagramme(word1, word2):
	l1 = list(word1)
	l2 = list(word2)
	l1.sort()
	l2.sort()
	return l1 == l2
print(f'sameLetter("chine", "chien"): {anagramme("chine", "chien")}')
