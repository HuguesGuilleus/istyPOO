#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from storage.struct import Struct as Struct
from storage.db import DB as DB

if not os.path.exists("data/"):
	os.makedirs("data/")

# Classes

class Guest(Struct):
	def __init__(self, db):
		super(Guest, self).__init__({
			"*Name": "",
			"tel": "",
			"mail": "",
			"desc": "",
		}, db)
GuestDB = DB("data/guest.db", Guest)

class Functionary(Struct):
	def __init__(self, db):
		super(Functionary, self).__init__({
			"*name": "",
			"info": "",
			"tel": "",
			"mail": "",
			"screening": [],
		}, db)
FunctionaryDB = DB("data/functionary.db", Functionary)

class Screening(Struct):
	def __init__(self, db):
		super(Screening, self).__init__({
			"*title": "",
			"location": b"",
			"guest": b"",
			"debate": False,
			"ticketAvailable": 0,
			"ticketSold": 0,
			"ticketBooked": 0,
			"todo": [],
		}, db)
ScreeningDB = DB("data/seance.db", Screening)

class Location(Struct):
	def __init__(self, db):
		super(Location, self).__init__({
			"*name": "",
			"addresse": "",
			"nbTicket": 0,
			"type": "cinema",
			"supervisor": b"",
		}, db)
	def getDB(self, key):
		if key == "supervisor":
			return FunctionaryDB
		return None
LocationDB = DB("data/location.db", Location)
