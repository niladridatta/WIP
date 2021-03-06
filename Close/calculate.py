#! /usr/bin/python3

import sys

# last = '20171213'

closes = [-6.3, 12.8, -1.8, 83.3, -30.0, -7.8, 52.6, 92.0, 26.6, -6.9, 12.4, -14.8, 19.0, 18.1, -85.8, 42.1, 84.3, 127.0, 38.5, -8.5, -71.5, 
155.1, 17.9, 6.7, 60.1, -32.8, 0.8, 9.4, 15.1, 11.5, -12.8, -67.6, 53.3, 43.7, 57.5, 28.6, 19.0, 12.6, -42.8, -17.1, 
66.2, -46.0, -2.2, 65.9, -16.6, -22.6, 2.7, 7.5, 152.5, -2.2, 68.9, 6.3, -33.2, -5.4, -91.0, 55.8, 21.7, -62.8, 55.6, 43.0, 30.0, 0.0, 
64.1, 27.3, -3.2, -63.7, -16.8, 55.5, -33.5, -52.7, -11.5, -34.1, -1.6, 32.9, -17.0, 98.6, 88.6, 45.2, -9.7, -38.1, 
9.8, -1.8, 47.9, -74.6, 28.8, 2.8, 90.4, 15.1, -21.5, 44.5, 66.9, 13.5, -96.3, -1.6, 10.4, -52.1, -25.6, 149.2, 85.4, 9.8, 19.6, -3.3, 
-5.1, 37.4, 21.6, -38.0, 26.8, -16.6, 21.0, -51.9, -9.5, 11.2, -40.1, 10.0, 69.5, -4.0, -19.9, -3.6, -55.0, -63.6, -20.1, 12.9, 16.8, 
94.1, -1.7, 24.3, 36.9, -8.8, 105.2, 15.0, 30.1, 75.6, -5.4, 29.6, -88.8, 72.5, -26.3, 42.0, 51.1, -1.9, 56.1, -0.1, -6.0, 62.6, 
37.5, -33.1, -67.9, 52.8, -9.0, -78.9, -70.5, -87.8, -109.5, 83.4, 103.1, 6.9, -66.8, -83.0, 11.2, 87.0, 4.5, 55.8, -116.8, 88.4, 33.5, 
56.5, -61.5, 39.4, -36.0, 13.7, 4.9, 71.2, 87.0, -13.8, 7.3, -1.2, 67.7, -5.6, -6.4, -19.2, -157.5, -91.8, -1.1, -135.8, 33.2, 19.6, 
70.9, 55.4, -26.2, 91.0, 9.0, 28.2, -32.2, 111.6, 71.1, 63.4, 3.6, -23.6, -64.3, 38.3, 22.9, 87.6, 48.4, -20.8, 40.6, -28.4, 
105.2, -16.7, 28.7, -0.7, -101.6, -47.0, 5.8, 12.8, -96.8, -38.4, -68.6, 96.7, 68.9, 15.1, 28.1, 15.4, 6.5, 41.0, 9.8, -29.3, -9.0, -134.8, 
-104.8, 6.0, -9.5, -74.1, 122.6, 98.9, 56.6, -82.1, -47.2 ]

last = len(closes)
arg_count = len(sys.argv)

def threshold():

	''' Returns the next day's and the next to next trading day's movement for a given threshold '''
	''' For cols = 2 => Returns the next day's movement only '''
	''' For cols = 3 => Returns the next day's and the next to next trading day's movement'''

	cols = 2
	contd = 0
	revsd = 0

	if arg_count == 1:
		low = -750
		high = 100

	if arg_count == 2:
		low = -750
		high = float(sys.argv[1])

	if arg_count == 3:
		low = float(sys.argv[2])
		high = float(sys.argv[1])

	print("\nHigh: %s\nLow: %s\n" % (high, low))
	
	for i in range(0, last):
		if closes[i] >= high and i < last - 1:
		
			if cols == 2:
				print("[%d]: %s => %s" % (i, closes[i], closes[i+1]))
			else:
				print("[%d]: %s => %s => %s" % (i, closes[i], closes[i+1], closes[i+2]))
				
			if closes[i+1] > 0:
				contd += 1
				print("Contd.")
			else:
				revsd += 1
				print("Revsd.")
			
		if closes[i] <= low and i < last - 1:
		
			if cols == 2:
				print("[%d]: %s => %s" % (i, closes[i], closes[i+1]))
			else:
				print("[%d]: %s => %s => %s" % (i, closes[i], closes[i+1], closes[i+2]))
				
			if closes[i+1] < 0:
				contd += 1
				print("Contd.\n")
			else:
				revsd += 1
				print("Revsd.\n")	

	print("Contd:", contd)
	print("Revsd:", revsd)
	
	
def trend():

	''' Returns the Max. Continuos Positive and Negative Trends '''
	
	up = 0
	dn = 0
	
	trend_pos = 0
	trend_neg = 0
	
	sum_pos = 0
	sum_neg = 0
	
	for i in range(0, last):
	
		if closes[i] >= 0:
			dn = 0
			up += 1
		else:
			up = 0
			dn += 1
		
		if up > trend_pos:
			trend_pos = up
			trend_pos_start = i - trend_pos + 1
			trend_pos_end = i
			
		if dn > trend_neg:
			trend_neg = dn
			trend_neg_start = i - trend_neg + 1
			trend_neg_end = i
			
	print("Positive Trend: ", trend_pos)
	print("Negative Trend: ", trend_neg)
	
	print("\nPositive Trend Range:\t%s .. %s\n" % (trend_pos_start, trend_pos_end))
	
	for j in range(trend_pos_start, trend_pos_end + 1):
		sum_pos += closes[j]
		print("%s, " % closes[j], end='')
	
	print("\nTotal: %s" % round(sum_pos, 1))

	print("\nPositive Trend Range:\t%s .. %s\n" % (trend_neg_start, trend_neg_end))
	
	for j in range(trend_neg_start, trend_neg_end + 1):
		sum_neg += closes[j]
		print("%s, " % closes[j], end='')
		
	print("\nTotal: %s" % round(sum_neg, 1))
		

print("\nDiff List: \n\n%s \n\nTotal: %s\n" % (closes, last))
	
# trend()

threshold()

print()










































