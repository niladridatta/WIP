#! /usr/bin/python3

import os
import csv
import datetime

cls_file = '/root/Downloads/close/close_nov.csv'

start_date = '20171113'
end_date = '20171117'

print("Start Date: ", start_date)
print("End Date: ", end_date)
print()

cls_file_hand = open(cls_file)
dat_reader = csv.reader(cls_file_hand)

for row in dat_reader:

	date = row[0]

	if date >= start_date and date <= end_date:
		print(date)
