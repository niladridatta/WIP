#! /usr/bin/python3

'''             Verify               '''

'''             prev_cls	     '''
'''             end_date	     '''
'''             start_date	     '''
'''             nifty_files          '''

import os
import csv
import datetime

nifty_dir = '/root/Downloads/nifty'
extension = '.csv'
print("Taking Nifty closing from", nifty_dir)

print()
print("Nifty DIR: ", nifty_dir)
nifty_files = os.listdir(nifty_dir)
print(nifty_files)
print()

cls_dir = '/root/Downloads/close'
print("Close DIR:", cls_dir)

os.chdir(nifty_dir)

for dat_file_name in nifty_files:
        if os.path.isfile(dat_file_name):

                month = dat_file_name[6:9]
                cls_file_name = "close_" + month + ".csv"

                dat_file = nifty_dir + "/" + dat_file_name
                cls_file = cls_dir + "/" + cls_file_name

                print("dat_file: ", dat_file)
                print("cls_file: ", cls_file)
                print()

                dat_file_hand = open(dat_file)
                dat_reader = csv.reader(dat_file_hand)

                cls_file_hand = open(cls_file, 'w')
                out_writer = csv.writer(cls_file_hand, lineterminator='\n')

                data = []
                prev_cls = 10335.3
                next(dat_reader)

                for row in dat_reader:

                                date_str = row[0]
                                date_date = datetime.datetime.strptime(date_str, "%d-%b-%Y").strftime("%Y%m%d")
                                
                                cur_cls = float(row[4].strip())
                                diff = cur_cls - prev_cls
                                rec = [date_date, prev_cls, cur_cls, round(diff,1)]
                                prev_cls = cur_cls

                                data.append(rec)
                                out_writer.writerow(rec)


                dat_file_hand.close()
                cls_file_hand.close()

                print("%s Closing: " % month.capitalize())
                print()

                for dat in data:
                        print(dat)

                print("\nRecords: ", len(data))
                print()

                start_date = '20171101'
                end_date = '20171131'

                date = []
                diff = []
                cur_cls = []
                prev_cls = []

                print("Start Date: ", start_date)
                print("End Date: ", end_date)

                cls_file_hand = open(cls_file)
                dat_reader = csv.reader(cls_file_hand)

                for row in dat_reader:

                        dt = row[0]

                        if dt >= start_date and dt <= end_date:
                                date.append(row[0])
                                prev_cls.append(row[1])
                                cur_cls.append(row[2])
                                diff.append(row[3])


                print("\n%s \n\n%s \n\n%s \n\n%s" % (date, prev_cls, cur_cls, diff))
                print("\nRecords : %d\n" % len(date))

