#! /usr/bin/python3

'''             Verify         	     '''

'''             dates          	     '''
'''             closes         	     '''
'''             totals         	     '''
'''             expiry               '''
'''             date_range           '''

import collections

dates = ['20171003', '20171004', '20171005', '20171006', '20171009', '20171010', '20171011', '20171012', '20171013', '20171016', '20171017', '20171018', '20171019', '20171023', '20171024', '20171025', '20171026', '20171027', '20171030', '20171031']

closes = ['9859.5', '9914.9', '9888.7', '9979.7', '9988.75', '10016.95', '9984.8', '10096.4', '10167.45', '10230.85', '10234.45', '10210.85', '10146.55', '10184.85', '10207.7', '10295.35', '10343.8', '10323.05', '10363.65', '10335.3']

totals = {

9500: [413.2, 454.7, 434.0, 515.2, 524.6, 541.4, 505.2, 612.3, 701.6, 758.1, 754.5, 738.2, 638.5, 690.2, 714.0, 784.0, 841.5],
9600: [339.4, 376.8, 353.2, 424.5, 432.7, 447.6, 424.5, 518.8, 603.0, 660.0, 656.6, 641.0, 551.9, 586.1, 615.1, 686.6, 745.2],
9700: [280.4, 302.1, 282.8, 344.7, 349.7, 360.1, 334.4, 424.6, 505.1, 560.5, 559.8, 544.4, 464.1, 489.9, 515.4, 586.4, 646.1],
9800: [238.6, 245.3, 230.2, 267.3, 274.4, 281.6, 260.4, 339.2, 414.9, 467.6, 464.2, 445.6, 356.8, 386.6, 418.0, 484.9, 543.0],
9900: [220.3, 207.4, 201.0, 210.3, 211.9, 213.9, 202.5, 256.2, 322.5, 374.6, 372.6, 357.1, 276.3, 295.2, 322.6, 386.7, 440.0],
10000: [233.6, 200.2, 201.3, 177.8, 173.7, 168.8, 167.6, 187.3, 242.7, 284.3, 279.8, 256.6, 193.2, 201.3, 224.7, 285.9, 336.9],
10100: [279.6, 228.5, 239.8, 184.7, 174.9, 162.9, 176.4, 149.2, 177.6, 202.8, 198.5, 176.5, 138.4, 127.8, 139.6, 190.3, 241.2],
10200: [350.6, 289.9, 306.0, 237.2, 219.9, 204.2, 229.6, 155.8, 143.4, 141.8, 140.5, 118.8, 124.8, 92.2, 89.4, 101.2, 137.4],
10300: [436.7, 378.4, 396.4, 309.7, 294.2, 276.1, 310.7, 209.2, 158.0, 127.4, 128.4, 119.2, 168.1, 126.7, 103.2, 56.6, 36.7],
10400: [529.2, 463.5, 494.8, 395.7, 386.2, 367.2, 404.4, 297.9, 221.8, 175.1, 173.2, 175.3, 250.8, 210.8, 179.4, 112.5, 51.6],
10500: [626.2, 569.6, 583.6, 500.7, 480.1, 462.1, 501.9, 390.1, 306.7, 249.8, 253.8, 265.0, 356.0, 310.4, 275.9, 205.8, 144.4],
10600: [727.8, 651.9, 669.2, 582.0, 573.4, 556.0, 588.4, 481.1, 404.9, 341.4, 345.9, 350.1, 470.0, 409.9, 376.1, 305.6, 251.5],
10700: [819.4, 754.7, 762.0, 692.4, 666.0, 666.0, 706.9, 588.7, 510.6, 452.3, 459.2, 458.8, 556.3, 520.9, 475.1, 411.1, 347.4],
10800: [941.9, 941.9, 879.8, 879.8, 786.7, 756.6, 798.6, 780.9, 591.4, 534.5, 533.8, 553.4, 553.4, 608.5, 608.4, 492.2, 476.7],
10900: [1021.0, 1021.0, 970.7, 903.4, 905.1, 905.1, 841.3, 812.5, 727.6, 632.5, 633.6, 654.4, 654.1, 654.1, 654.0, 590.3, 541.3],

}

expiry_dates = ['26-Oct-2017', '30-Nov-2017', '28-Dec-2017']
expiry = expiry_dates[0]

orderd_totals =  collections.OrderedDict(sorted(totals.items()))

# print("\nClose:\n\n%s" % closes)

# print("\nTotal:\n")

# for k,v in orderd_totals.items():
# 	print("%s => %s" % (k, v))

print()

date_ranges = [[('20171003', '20171010'), ('20171010', '20171019'), ('20171019', '20171026'), ('20171003', '20171026')],
		[('20171101', '20171110'), ('20171110', '20171120'), ('20171120', '20171130'), ('20171101', '20171130')],
]

date_range = date_ranges[0]

for dr in date_range:

	start_date = dr[0]
	end_date = dr[1]

	if start_date in dates:
		start_index = dates.index(start_date)

	if end_date in dates:
		end_index = dates.index(end_date)

	close_start = float(closes[start_index]) 
	close_end = float(closes[end_index])

	close_diff = close_end - close_start

	print("Diff From: %s to %s\t\tExpiry: %s" % (start_date, end_date, expiry))

	print("Nifty:\t\t%s\n" % (round(close_diff,1)))

	keys = []
	diff = []

	for k,v in orderd_totals.items():

		total_start = totals[k][start_index]
		total_end = totals[k][end_index]

		total_diff = round((total_end - total_start),1)

		keys.append(k)
		diff.append(total_diff)
		
	print("%s\n%s" % (keys, diff))
	print()


