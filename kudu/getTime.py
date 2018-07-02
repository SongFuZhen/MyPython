#!/usr/bin/python3.4
# coding=utf-8

import datetime
import time
import random
import csv
import os;
import sys

# define const
BEGIN = '2018-07-01 00:00:00'
END = '2018-07-10 23:59:59'

# convert to timestamp
# startTimeStamp = int(time.mktime(time.strptime(BEGIN, "%Y-%m-%d %H:%M:%S")))
# endTimeStamp = int(time.mktime(time.strptime(END, "%Y-%m-%d %H:%M:%S")))

# timeStampData = []

# print(startTimeStamp, endTimeStamp)
# time = startTimeStamp
# while (time <= endTimeStamp):
#     print(time)
#     time = time + 86400

timeArray = time.localtime(1530374400)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
# otherStyletime == "2013-10-10 23:40:00"

print(otherStyleTime )



ALTER TABLE table_name ADD RANGE PARTITION partition_condatition