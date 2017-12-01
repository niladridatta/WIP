#! /usr/bin/python3

import os
import csv
import sqlite3
import subprocess

drop = 'NO'
table_name = 'test_sep'
db_name = 'example.db'
out_dir = '/root/Downloads/output'

print("Output DIR:")
out_files = [file for file in os.listdir(out_dir) if file.endswith(".csv")]
print(out_files)
print()

print("DB: ", db_name)
print("Table: ", table_name)

os.chdir(out_dir)
db_path = os.getcwd()
print("DB Path: ", db_path)
print()

for dat_file_name in out_files:
	if os.path.isfile(dat_file_name):

		dat_file = out_dir + "/" + dat_file_name
	
		print("dat_file: ", dat_file)
		print()
	
		dat_file_hand = open(dat_file)
		dat_reader = csv.reader(dat_file_hand)
	
		next(dat_reader)
	
		conn = sqlite3.connect(db_name)
	
		c = conn.cursor()

		if drop == 'YES':
	
			# Drop table if exists
			print("Dropping TABLE:", table_name)
			print()

			drop = 'NO'

		## ["SYMBOL", "INSTRUMENT", "EXPIRY_DT", "STRIKE_PR", "OPTION_TYP", "CLOSE", "OPEN_INT", "CHG_IN_OI", "TIMESTAMP"]
	
		# Create table
		c.execute('CREATE TABLE IF NOT EXISTS test_sep (SYMBOL text, INSTRUMENT text, EXPIRY_DT test, STRIKE_PR real, OPTION_TYP text, CLOSE real, CHG_IN_OI real, OPEN_INT real, TIMESTAMP text)')
	
		# Display table
		for row in c.execute('SELECT * FROM test_sep ORDER BY EXPIRY_DT, STRIKE_PR'):
			print(row)
	
		# Populate table
		for row in dat_reader:
			c.execute('INSERT INTO test_sep VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', row)
	
		conn.commit()
	
# Display table
for row in c.execute('SELECT * FROM test_sep ORDER BY EXPIRY_DT, STRIKE_PR'):
	print(row)
	
# Count records
c.execute('SELECT * FROM test_sep')
records = c.fetchall()
conn.close()
	
print("\nRecords: ", len(records))
print()

