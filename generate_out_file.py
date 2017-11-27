#! /usr/bin/python3

import os
import csv
import zipfile
import datetime

bhav_dir = '/root/Downloads/bhav'
extension = '.zip'
print("Taking Bhavs from", bhav_dir)

print()
print("Bhav DIR:")
bhav_files = os.listdir(bhav_dir)
print(bhav_files)
print()

extract_dir = '/root/Downloads/extracted'
print("Extracting to", extract_dir)
print()

os.chdir(bhav_dir)

for file in os.listdir(bhav_dir):
	if os.path.isfile(file) and file.endswith(extension):
		file_name = os.path.abspath(file)
		zip_ref = zipfile.ZipFile(file_name)
		zip_ref.extractall(extract_dir)
		zip_ref.close()

print("Extract DIR:")
extracted_files = os.listdir(extract_dir)
print(extracted_files)
print()

out_dir = '/root/Downloads/output'

os.chdir(extract_dir)

for dat_file_name in extracted_files:
	if os.path.isfile(dat_file_name):

		date = dat_file_name[2:11]
		out_file_name = "out_" + date + ".csv"
	
		dat_file = extract_dir + "/" + dat_file_name
		out_file = out_dir + "/" + dat_file_name
	
		print("dat_file: ", dat_file)
		print("out_file: ", out_file)
		print()
	
		dat_file_hand = open(dat_file)
		dat_reader = csv.reader(dat_file_hand)
	
		out_file_hand = open(out_file, 'w')
		out_writer = csv.writer(out_file_hand, lineterminator='\n')
	
		data = []
	
		data.append(["SYMBOL", "INSTRUMENT", "EXPIRY_DT", "STRIKE_PR", "OPTION_TYP", "CLOSE", "OPEN_INT", "CHG_IN_OI", "TIMESTAMP"])
		out_writer.writerow(["SYMBOL", "INSTRUMENT", "EXPIRY_DT", "STRIKE_PR", "OPTION_TYP", "CLOSE", "OPEN_INT", "CHG_IN_OI", "TIMESTAMP"])
	
		cur_str = 10200
		low_str = cur_str - 700
		upr_str = cur_str + 700
	
		cur_exp = '30-Nov-2017'
		nxt_exp = '28-Dec-2017'
	
		for row in dat_reader:
			if ( row[1].strip() == 'NIFTY' and ( int(row[3]) % 100 == 0 ) and row[2] == cur_exp) or ( row[1].strip() == 'NIFTY' and ( int(row[3]) % 100 == 0 ) and row[2] == nxt_exp):
	
				SYMBOL = row[1]
				EXPIRY_DT = row[2]
				INSTRUMENT = row[0]
				STRIKE_PR = int(float(row[3]))
				OPTION_TYP = row[4]
				CLOSE = float(row[8])
				OPEN_INT = int(row[12])
				CHG_IN_OI = int(row[13])
	
				date_str = row[14]
				date_date = datetime.datetime.strptime(date_str, "%d-%b-%Y").strftime("%Y-%m-%d")
				TIMESTAMP = date_date
	
				if STRIKE_PR >= low_str and STRIKE_PR <= upr_str:
	
					data.append([SYMBOL, INSTRUMENT, EXPIRY_DT, STRIKE_PR, OPTION_TYP, CLOSE, OPEN_INT, CHG_IN_OI, TIMESTAMP])
					out_writer.writerow([SYMBOL, INSTRUMENT, EXPIRY_DT, STRIKE_PR, OPTION_TYP, CLOSE, OPEN_INT, CHG_IN_OI, TIMESTAMP])
	
		dat_file_hand.close()
		out_file_hand.close()
	
		for dat in data:
			print(dat)
	
		print("\nRecords: ", len(data) - 1)
		print()

