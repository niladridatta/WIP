#! /usr/bin/python3

date_nov = ['20171101', '20171102', '20171103', '20171106', '20171107', '20171108', '20171109', '20171110', '20171113', '20171114', '20171115', '20171116', '20171117', '20171120', '20171121', '20171122', '20171123', '20171124', '20171127', '20171128', '20171129', '20171130']

close_nov = ['10440.5', '10423.8', '10452.5', '10451.8', '10350.15', '10303.15', '10308.95', '10321.75', '10224.95', '10186.6', '10118.05', '10214.75', '10283.6', '10298.75', '10326.9', '10342.3', '10348.75', '10389.7', '10399.55', '10370.25', '10361.3', '10226.55']

total_nov = {
	9500: [978.0, 955.6, 982.6, 988.9, 912.2, 847.2, 861.7, 821.2, 767.6, 743.9, 659.8, 746.5, 804.2, 825.0, 852.9, 855.2, 863.5, 906.0, 915.2, 874.8, 859.2, 730.5]	    }

print("\nDate:\n\n%s" % date_nov)
print("\nClose:\n\n%s" % close_nov)

for k,v in total_nov.items():
	print("\nTotal:\n\n%s => %s" % (k, v))

start_date = '20171101'
end_date = '20171130'

if start_date in date_nov:
	start_index = date_nov.index(start_date)

if end_date in date_nov:
	end_index = date_nov.index(end_date)

if start_index is not None and end_index is not None:
	print("\nStr Date: %s \t\t Str Index: %d" % (start_date, start_index))
	print("End Date: %s \t\t End Index: %d" % (end_date, end_index))

close_start = float(close_nov[start_index]) 
close_end = float(close_nov[end_index])

close_diff = close_start - close_end

print("\nClose Start: %s \t\t Close End: %s" % (close_start, close_end))
print("Close Diffr: %s" % (round(close_diff,1)))

total_start = total_nov[9500][start_index]
total_end = total_nov[9500][end_index]

total_diff = total_start - total_end

print("\nTotal Start: %s \t\t Total End: %s" % (total_start, total_end))
print("Total Diffr: %s\n" % (total_diff))

