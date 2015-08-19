#!/usr/bin/env python
'''
script to parse failed Cisco ISE authentication log and output only rows with unique mac addresses.
'''
__author__ = 'Justin Bollinger'
import csv
import sys

uniquemac = []
with open(sys.argv[1]) as csvfile:
    parser = csv.reader(csvfile, dialect='excel')
    #parser.next()   # remove header
    for row in parser:
        if uniquemac.count(row[16]) == 0:
            print row
            uniquemac.append(row[16])


