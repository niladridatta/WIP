#! /usr/bin/python3

import collections

date_nov = ['20171101', '20171102', '20171103', '20171106', '20171107', '20171108', '20171109', '20171110', '20171113', '20171114', '20171115', '20171116', '20171117', '20171120', '20171121', '20171122', '20171123', '20171124', '20171127', '20171128', '20171129', '20171130']

close_nov = ['10440.5', '10423.8', '10452.5', '10451.8', '10350.15', '10303.15', '10308.95', '10321.75', '10224.95', '10186.6', '10118.05', '10214.75', '10283.6', '10298.75', '10326.9', '10342.3', '10348.75', '10389.7', '10399.55', '10370.25', '10361.3', '10226.55']

total_nov = {

9500: [978.0, 955.6, 982.6, 988.9, 912.2, 847.2, 861.7, 821.2, 767.6, 743.9, 659.8, 746.5, 804.2, 825.0, 852.9, 855.2, 863.5, 906.0, 915.2, 874.8, 859.2, 730.5],
9600: [882.6, 859.6, 886.8, 907.5, 821.4, 759.0, 763.0, 754.1, 681.2, 637.2, 564.1, 666.6, 709.4, 727.0, 757.9, 754.8, 761.4, 806.0, 817.9, 772.0, 762.1, 634.0],
9700: [787.5, 767.0, 793.0, 789.9, 728.8, 653.3, 662.1, 647.4, 583.3, 542.6, 464.8, 545.0, 615.4, 622.5, 649.1, 654.6, 668.1, 706.2, 715.0, 673.7, 659.0, 541.6],
9800: [701.4, 669.0, 702.7, 702.4, 638.5, 584.4, 578.9, 561.0, 494.5, 455.6, 388.3, 458.6, 520.1, 526.1, 551.0, 557.7, 568.9, 603.6, 613.8, 577.2, 569.6, 428.5],
9900: [609.5, 586.9, 610.7, 630.6, 551.2, 493.9, 492.0, 467.1, 408.4, 371.8, 306.9, 373.7, 419.9, 427.6, 456.8, 463.8, 470.8, 509.7, 515.9, 472.2, 455.6, 324.5],
10000: [523.0, 499.1, 526.0, 532.6, 465.4, 412.2, 405.5, 385.4, 334.0, 296.2, 241.2, 289.2, 335.7, 336.8, 362.4, 364.6, 372.4, 413.9, 416.2, 374.6, 358.9, 224.5],
10100: [444.2, 417.5, 438.4, 445.9, 385.2, 335.2, 330.4, 307.6, 270.1, 238.6, 202.2, 220.2, 256.7, 255.0, 277.6, 276.7, 277.4, 318.8, 320.4, 279.3, 258.8, 127.1],
10200: [371.2, 345.6, 364.4, 376.4, 316.2, 276.6, 265.4, 246.8, 228.2, 206.9, 192.2, 176.9, 196.2, 190.6, 200.9, 199.4, 198.6, 228.4, 227.5, 186.1, 164.3, 28.9],
10300: [308.2, 284.9, 296.3, 301.9, 266.9, 234.8, 221.8, 218.2, 213.7, 204.2, 220.1, 172.6, 166.2, 154.4, 150.4, 144.7, 138.1, 153.1, 141.1, 109.6, 83.4, 62.1],
10400: [267.4, 247.7, 248.4, 257.9, 238.1, 223.9, 210.1, 212.9, 229.5, 235.0, 277.2, 207.1, 178.9, 166.2, 146.7, 135.6, 124.2, 109.8, 89.3, 80.4, 65.6, 163.9],
10500: [247.5, 233.4, 223.0, 231.1, 236.8, 241.3, 230.6, 240.7, 276.9, 294.6, 353.6, 271.8, 226.1, 216.8, 186.6, 176.8, 163.7, 127.0, 107.0, 129.0, 134.2, 259.1],
10600: [253.9, 248.8, 225.9, 232.6, 265.8, 289.6, 280.3, 305.7, 346.2, 369.8, 445.7, 350.6, 305.1, 293.4, 257.7, 250.0, 236.9, 194.7, 178.4, 218.2, 224.2, 363.2],
10700: [292.0, 295.0, 267.9, 268.9, 324.0, 353.7, 352.6, 380.4, 431.0, 464.4, 538.1, 451.2, 383.5, 372.2, 346.4, 337.1, 325.0, 286.4, 279.2, 317.4, 327.7, 468.6],
10800: [343.6, 363.6, 334.7, 341.2, 400.4, 442.8, 443.8, 450.1, 523.9, 558.4, 642.5, 536.2, 487.2, 477.5, 451.9, 438.1, 419.9, 381.6, 376.8, 415.2, 424.3, 560.6],
10900: [427.5, 444.9, 419.9, 416.2, 490.4, 539.9, 559.0, 587.4, 618.2, 658.7, 758.0, 663.5, 579.0, 581.8, 538.8, 531.2, 573.8, 470.5, 520.6, 516.5, 537.2, 650.2],

}

orderd_total_nov =  collections.OrderedDict(sorted(total_nov.items()))

# print("\nClose:\n\n%s" % close_nov)

# print("\nTotal:\n")

# for k,v in orderd_total_nov.items():
# 	print("%s => %s" % (k, v))

date_ranges = [('20171101', '20171110'), ('20171111', '20171120'), ('20171121', '20171130'), ('20171101', '20171130')]

for dr in date_ranges:

	start_date = dr[0]
	end_date = dr[1]

	if start_date in date_nov:
		start_index = date_nov.index(start_date)

	if end_date in date_nov:
		end_index = date_nov.index(end_date)

	close_start = float(close_nov[start_index]) 
	close_end = float(close_nov[end_index])

	close_diff = close_end - close_start

	print("\nDiff From: %s to %s" % (start_date, end_date))

	print("\nNifty:\t\t%s\n" % (round(close_diff,1)))

	keys = []
	diff = []

	for k,v in orderd_total_nov.items():

		total_start = total_nov[k][start_index]
		total_end = total_nov[k][end_index]

		total_diff = round((total_end - total_start),1)

		keys.append(k)
		diff.append(total_diff)
		
	print("%s\n%s" % (keys, diff))
	print()


