#! /usr/bin/python3

import re

processed_dir = '/root/Processed'
filename = 'processed_nov'

file = processed_dir + "/" + filename
print(file)

with open(file) as f_in:
    lines = (line.rstrip() for line in f_in) # All lines including the blank ones
#    lines = (line for line in lines if line) # Non-blank lines

for line in lines:
	print(line)

exit()

file_hand = open(file)

for line in file_hand:

	if re.search('\S', line) and line != '\n':
		print(line)

