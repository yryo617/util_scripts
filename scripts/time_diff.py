#!/usr/bin/env python

import sys
import math
import string

colon=":"
hoursec=3600
minsec=60


def timediff(t1, t2):
    t1sec = timesec(t1)
    t2sec = timesec(t2)

    tdiffsec=t1sec-t2sec

    tdiffsec=abs(tdiffsec)
    tdiffstr=sectime(tdiffsec)

    return tdiffstr

def timesec(t):
    tsplit = string.split(t,colon)
    if(len(tsplit)==1):
        tsplit.append("00")
    if(len(tsplit)==2):
        tsplit.append("00")

    tsec= int(tsplit[0])*hoursec
    tsec+= int(tsplit[1])*minsec
    tsec+= int(tsplit[2])
    tsec = int(tsec)
    return tsec

def sectime(tsec):
    hr=tsec/hoursec
    min=(tsec%hoursec)/minsec
    sec=(tsec%hoursec%minsec)
    # print "{}:{}:{}".format(hr,min,sec)
    tstr="{0:02d}:{1:02d}:{2:02d}".format(hr,min,sec)
    return tstr

#-------------------------------------------#


time1 = sys.argv[1]
time2 = sys.argv[2]

print "times: {} and {}".format(time1,time2)

print timediff(time1,time2)
