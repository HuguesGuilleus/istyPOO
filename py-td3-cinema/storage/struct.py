#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
from hashlib import sha256
import json

class Struct:
	"""Un classe pour standardiser une structure, ainsi tous accès en lecture
	ou écriture à des champs non définis à l'initialisation de Struct lèveront
	une exeption.
	"""
	def __init__(self, keys, db):
		"""keys doit être un dictionnaire. La clé doit être une chaîne de
		caractère. La valeur n'a pas de type défini, mais elle doit pouvoir
		être enregistrée en JSON; la valeur fournie servira de valeur par
		défaut et à définir le type lors des affectations.

		Une des clés doit commencé par un astérix, elle définira la clé qui
		servira à générer l'identificant."""
		self.db = db
		self.idValue = ""
		self.idKey = ""
		for k, v in keys.copy().items():
			if type(k) != type(""):
				raise TypeError("Struct expect string key")
			if k[0] == "*":
				del keys[k]
				self.idKey = k[1:]
				self.idValue = v
		if self.idKey == "":
			raise LookupError("Need a ID key")
		self.templ = keys
		self.values = self.templ.copy()
		self.setId(self.idValue)

	def toJSON(self):
		cp = self.values.copy()
		cp[self.idKey] = self.idValue
		for k in cp.copy():
			if type(cp[k]) == type(b''):
				cp[k] = str(base64.encodebytes(cp[k]))
		return json.dumps(cp)
	def fromJSON(self, j):
		self.values = self.templ.copy()
		values = json.loads(j)
		for k, v in values.items():
			if type(v) == type(b"") and type(self[k]) == type(""):
				v = base64.decodebytes(v)
			elif k == self.idKey and type(self.idValue) == type(v):
				self.setId(v)
			elif k in self.values and type(v) == type(self[k]):
				self[k] = v
		return self
	def setId(self, v):
		"Regénère l'identifiant de l'objet."
		if type(self.idValue) != type(v):
			raise TypeError(f"'{v}' have not the type {type(self.idValue)}")
		self.idValue = v
		self.id = bytes(sha256(bytes(v, "utf-8")).hexdigest()[:15], "utf-8")
	def save(self):
		"Sauvegarde dans la db."
		self.db.set(self)

	def __str__(self):
		c = self.__class__.__name__
		s = f"<{c}:{self.id} {self.idKey}={self.idValue!r}"
		for k, v in self.values.items():
			s += f" {k}={v!r}"
		return s + ">"
	def __iter__(self):
		return iter(self.values.items())
	def __getitem__(self, k):
		"""Récupère une valeur qui peut être l'identifiant."""
		if k not in self.values:
			raise KeyError(f"The key '{k}' is not in this Struct")
		return self.values[k]
	def __setitem__(self, k, v):
		"""Change une valeur, dont la clé et le type attendu sont défini à
		l'initialisation. Ne l'accède pas à la valeur de l'identifiant."""
		if k not in self.values:
			raise KeyError(f"The key '{k}' is not in this Struct")
		if type(v) != type(self.values[k]):
			raise TypeError(f"'{v}' have not the type {type(self.values[k])}")
		self.values[k] = v
	def getDB(self, key):
		"Retourne la base de donnée en relation avec une clé particulière"
		return None
	def autoremove(self):
		del self.db[self.id]
