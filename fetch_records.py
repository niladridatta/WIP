#! /usr/bin/python3

'''		Verify			'''

'''		expiry			'''
'''		table_name		'''
'''		lower_strike		'''
'''		upper_strike		'''

import os
import sqlite3
import collections
from operator import add

opt_type = ['CE', 'PE']
strike = []

lower_strike = 9500
upper_strike = 10900

expiry_dates = ['26-Oct-2017', '30-Nov-2017', '28-Dec-2017']
expiry = expiry_dates[2]

for strk in range(lower_strike, upper_strike + 100, 100):
	strike.append(strk)

print(strike)
print()

table_name = 'Nov_2017'
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

# print("Records:")
# print()

dict = {}
total = {}
nov_tot = {}

for s in strike:
	Nov_CE = []
	Nov_PE = []

	for opt in opt_type:
	
		if opt == 'CE':
			c.execute("SELECT SYMBOL, INSTRUMENT, EXPIRY_DT, STRIKE_PR, OPTION_TYP, CLOSE, TIMESTAMP FROM Nov_2017 WHERE EXPIRY_DT = ? AND STRIKE_PR = ? AND OPTION_TYP = ? ORDER BY TIMESTAMP", (expiry, s, opt))
		
			records = c.fetchall()
		
			for rec in records:
#				print(rec)
				Nov_CE.append(rec[5])
	
		if opt == 'PE':
			c.execute("SELECT SYMBOL, INSTRUMENT, EXPIRY_DT, STRIKE_PR, OPTION_TYP, CLOSE, TIMESTAMP FROM Nov_2017 WHERE EXPIRY_DT = ? AND STRIKE_PR = ? AND OPTION_TYP = ? ORDER BY TIMESTAMP", (expiry, s, opt))
		
			records = c.fetchall()

			for rec in records:
#				print(rec)
				Nov_PE.append(rec[5])

		key = str(s) + opt

		if opt == 'CE':
			dict[key] = Nov_CE

		if opt == 'PE':
			dict[key] = Nov_PE

	nov_tot[s] = list(map(add, Nov_CE, Nov_PE))

conn.close()

print("Daily Close for Expiry: ", expiry)
print()

orderd_dict = collections.OrderedDict(sorted(dict.items()))

for k,v in orderd_dict.items():
  print(k, v)

rnd_tot = {}

for k,v in nov_tot.items():
  rnd_tot_val = []

  for i in range(0, len(v)):
    rnd_tot_val.append(round(v[i],1))

  rnd_tot[k] = rnd_tot_val

print("\nRounded Daily Total for Expiry: ", expiry)
print()

orderd_rnd_tot = collections.OrderedDict(sorted(rnd_tot.items()))

for k,v in orderd_rnd_tot.items():
  print("%s: %s," % (k, v))

print("\nRounded Total Items: ", len(v))
print()

