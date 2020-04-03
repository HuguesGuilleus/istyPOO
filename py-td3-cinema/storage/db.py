#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dbm
import re


class DB:
	def __init__(self, name, cl):
		self.n = name
		self.cl = cl
		self.db = dbm.open(name, 'c')
	def __getitem__(self, key):
		return self.cl(self).fromJSON(self.db[key])
	def __setitem__(self, key, value):
		self.db[key] = value.toJSON()
	def set(self, obj):
		self.db[obj.id] = obj.toJSON()
	def __contains__(self, key):
		return key in self.db
	def __delitem__(self, key):
		del self.db[key]
	def __iter__(self):
		return iter(self.db.keys())
	def items(self):
		it = []
		for k in self:
			it.append((k,self[k]))
		return iter(it)
	def new(self):
		"Create a new empty struct attach to this DB"
		return self.cl(self)
	def name(self):
		return re.split("[/.]", self.n)[1]
