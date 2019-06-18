#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import datetime
import csv
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1015()

f = open('wavout.csv', 'w')
writer = csv.writer(f, lineterminator='\n')

GAIN = 1
sps = 128

msg = []

# LOOP
roop_cy = 1000
timetmp=datetime.datetime.now()
for a in range(roop_cy):

	csvlist = []
	strtmp=str(datetime.datetime.now()-timetmp)
	csvlist.append(strtmp[5:])
	csvlist.append(adc.read_adc(0, gain=GAIN, data_rate=sps))
	writer.writerow(csvlist)
	#time.sleep(0.05)
f.close()
