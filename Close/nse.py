#! /usr/bin/python3

import csv
import datetime

file = 'nse_test.csv'

file_hand = open(file)
reader = csv.reader(file_hand)

dict = {}
next(reader)

expiries = ['25-Jan-2017', '23-Feb-2017', '30-Mar-2017', '27-Apr-2017', '25-May-2017', '29-Jun-2017', '27-Jul-2017', '31-Aug-2017', '28-Sep-2017', '26-Oct-2017', '30-Nov-2017', '28-Dec-2017']

print("\nExpiry Dates:\n")
for exp in expiries:
	print("%s " % datetime.datetime.strptime(exp, "%d-%b-%Y").strftime("%Y%m%d"), end='')

print()

for row in reader:

	date_str = row[0]
	date_date = datetime.datetime.strptime(date_str, "%d-%b-%Y").strftime("%Y%m%d")

	opn = row[1].lstrip()
	hgh = row[2].lstrip()
	low = row[3].lstrip()
	cls = row[4].lstrip()
	trd = row[5].lstrip()
	trn = row[6].lstrip()

	dict[date_date] = [opn, hgh, low, cls, trd, trn]

file_hand.close()

# for (k,v) in dict.items():
#	print(k, v)

prev_cls = 8185.80
rnd_diff = {}

for (k,v) in dict.items():

	cur_cls = dict[k][3]
	diff = float(cur_cls) - float(prev_cls)
	rnd_diff[k] = round(diff, 1)

	prev_cls = cur_cls

vals = []
dates = []
month = '201701'

trd_date = {}
mon_diff = {}

for (k,v) in rnd_diff.items():

	mon = k[:6]

	if (month == mon):
		dates.append(k)
		vals.append(v)
	else:
		dates = []
		vals = []
		month = mon
		dates.append(k)
		vals.append(v)

	trd_date[mon] = dates
	mon_diff[mon] = vals

for k1,v1 in trd_date.items():
	for k2,v2 in mon_diff.items():
		if(k1 == k2):
#			print("\n%s: %s" % (k1, v1))
			print("%s: %s" % (k2, v2))

