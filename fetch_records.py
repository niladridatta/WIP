#! /usr/bin/python3

import os
import sqlite3
from operator import add

Nov_CE = []
Nov_PE = []
opt_type = ['CE', 'PE']
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

for opt in opt_type:

	if opt == 'CE':
		c.execute("SELECT SYMBOL, INSTRUMENT, EXPIRY_DT, STRIKE_PR, OPTION_TYP, CLOSE, TIMESTAMP FROM Nov_3 WHERE EXPIRY_DT='30-Nov-2017' AND STRIKE_PR=10000 AND OPTION_TYP = ? ORDER BY TIMESTAMP", (opt,))
	
		records = c.fetchall()
	
		for rec in records:
			print(rec)
			Nov_CE.append(rec[5])

	if opt == 'PE':
	        c.execute("SELECT SYMBOL, INSTRUMENT, EXPIRY_DT, STRIKE_PR, OPTION_TYP, CLOSE, TIMESTAMP FROM Nov_3 WHERE EXPIRY_DT='30-Nov-2017' AND STRIKE_PR=10000 AND OPTION_TYP = ? ORDER BY TIMESTAMP", (opt,))
	
	        records = c.fetchall()
	
	        for rec in records:
	                print(rec)
	                Nov_PE.append(rec[5])


print()
print("Nov_CE:")
print(Nov_CE)
print()
print("Nov_PE:")
print(Nov_PE)
print()

Nov_tot = list(map(add, Nov_CE, Nov_PE))
print("Nov_tot:")
print(Nov_tot)

conn.close()
print()

