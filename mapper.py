#!/usr/bin/env python

import sys

#file = open("all_month.csv")

def findRangeLat(a):
    a = round(a,0)
    for i in range(0,5):
        if (a-i)%5 == 0:
            return "latitude range(" + str(a-i) + " to " + str(a-i+5) + ")"
# input comes from STDIN (standard input)

for line in sys.stdin.readlines():
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(',')
    #print words
    # increase counters
    
    #for latitude
    '''if words[1]:
                    temp = findRangeLat(float(words[1]))
                    print '%s\t%s' % (temp, 1)
            
                #for magnitude
                try:
                    words[4] = float(words[4])
                    #print words[4]
                    temp = "magnitude range(" + str(round(float(words[4]),0)) + " to " + str(round(float(words[4]),0) + 1) + ")"
                    print '%s\t%s' % (temp, 1)
                except ValueError:
                    # count was not a number, so silently
                    # ignore/discard this line
                    continue'''

    #for day
    day = words[0].split("T")[0]
    print '%s\t%s' % (day, words[4])