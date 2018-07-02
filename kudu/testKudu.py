#!/usr/bin/python3.4
# coding=utf-8

import datetime
import time
import random
import csv
import os;
import sys

# define const
MACHINECOUNT = 10
MERTICCOUNT = 10
BEGIN = '2018-07-01 00:00:00'
END = '2018-07-10 00:00:00'

# define machineList
machineList = []
for i in range(MACHINECOUNT):
    machineTemp = 'machine00%s' % (i)
    machineList.append(machineTemp)

# define merticList
merticList = []
for i in range(MERTICCOUNT):
    merticTemp = 'metric00%s' % (i)
    merticList.append(merticTemp)

# generate data
# convert to timestamp
startTimeStamp = int(time.mktime(time.strptime(BEGIN, "%Y-%m-%d %H:%M:%S")))
endTimeStamp = int(time.mktime(time.strptime(END, "%Y-%m-%d %H:%M:%S")))

for machineIndex in range(len(machineList)):
    for merticIndex in range(len(merticList)):
        machineMerticData = []
        for i in range(endTimeStamp - startTimeStamp):
            dataTuple = (machineList[machineIndex], merticList[merticIndex], startTimeStamp + i, float('%.2f' % random.uniform(0, 1)))
            machineMerticData.append(dataTuple)

        print(machineMerticData)
        with open(machineList[machineIndex] + '_' + merticList[merticIndex] + '.csv', 'w') as csvout:
            writer = csv.writer(csvout)
            writer.writerows(machineMerticData)
            csvout.close()

    # csvfile = open(machineList[machineIndex] + '.csv', 'wb')
    # writer = csv.writer(csvfile)
    # writer.writerow([b'title', b'summary', b'year', b'id', b'count', b'link'])
    # writer = csv.writer(sys.stdout)
    # for item in machineData:
    #     writer.writerow(item)
    # writer.writerows(machineData)
    # csvfile.close()
