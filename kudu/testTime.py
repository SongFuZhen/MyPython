#!/usr/bin/python
# -*- encoding: utf-8 -*-

import time
import  datetime

BEGIN = '2018-07-01 00:00:00'
END = '2018-07-10 23:59:59'

startTimeStamp = int(time.mktime(time.strptime(BEGIN, "%Y-%m-%d %H:%M:%S")))
endTimeStamp = int(time.mktime(time.strptime(END, "%Y-%m-%d %H:%M:%S")))

print(startTimeStamp, endTimeStamp)
i = startTimeStamp
while i < endTimeStamp:
    m = i + 86400
    for j in range(10):
        for c in range(10):
            print('insert into metrics select * from metrics_raw where host = "machine00%d" and metric = "metric00%d" and %d <= time < %d;' %(j,c,i,m))
    i += 86400











