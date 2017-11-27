#! /usr/bin/python3

import os
import sqlite3
from operator import add
from pprint import pprint

opt_type = ['CE', 'PE']
strike = []

for strk in range(10000, 10600, 100):
	strike.append(strk)

print(strike)
print()

table_name = 'Nov_3'
db_name = 'example.db'

print("DB: ", db_name)
print("Table: ", table_name)

out_dir = '/root/Downloads/output'
os.chdir(out_dir)
db_path = os.getcwd()
print("DB Path: ", db_path)
print()

conn = sqlite3.connect(db_name)
c = conn.cursor()

print("Records:")
print()

dict = {}
total = {}
Nov_TOT = {}

for s in strike:
	Nov_CE = []
	Nov_PE = []

	for opt in opt_type:
	
		if opt == 'CE':
			c.execute("SELECT SYMBOL, INSTRUMENT, EXPIRY_DT, STRIKE_PR, OPTION_TYP, CLOSE, TIMESTAMP FROM Nov_3 WHERE EXPIRY_DT='30-Nov-2017' AND STRIKE_PR = ? AND OPTION_TYP = ? ORDER BY TIMESTAMP", (s, opt))
		
			records = c.fetchall()
		
			for rec in records:
				print(rec)
				Nov_CE.append(rec[5])
	
		if opt == 'PE':
			c.execute("SELECT SYMBOL, INSTRUMENT, EXPIRY_DT, STRIKE_PR, OPTION_TYP, CLOSE, TIMESTAMP FROM Nov_3 WHERE EXPIRY_DT='30-Nov-2017' AND STRIKE_PR = ? AND OPTION_TYP = ? ORDER BY TIMESTAMP", (s, opt))
		
			records = c.fetchall()

			for rec in records:
				print(rec)
				Nov_PE.append(rec[5])

		key = str(s) + opt

		if opt == 'CE':
			dict[key] = Nov_CE

		if opt == 'PE':
			dict[key] = Nov_PE

	Nov_TOT[s] = list(map(add, Nov_CE, Nov_PE))

print("\nDaily Close:\n")
pprint(dict)
print("\nDaily Total:\n")
pprint(Nov_TOT)
print()

conn.close()
print()

