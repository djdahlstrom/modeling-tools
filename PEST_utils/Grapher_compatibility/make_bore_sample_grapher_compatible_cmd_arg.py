# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 11:37:27 2012

script to make tab-delimited bore sample file
whitespace between date and time is a space so Grapher will not parse them as separate columns

if multiple wells occur, write to separate files, otherwise the input file is overwritten in place

@author: djd
https://github.com/djdahlstrom
"""
import sys

try:
    infile = sys.argv[1]
    print 'Opening file ', infile
    in1 = open(infile,'r')

except:
    print 'File name not given on command line. Assuming bob.dat'
    in1 = open('bob.dat', 'r')

contents = in1.readlines()
in1.close()

well = ''
out1 = open('bob2.dat', 'w')
for j in contents:
    line = j.split()
    # print line to filtered file without newline char
    if line[0] != well:
        out1.close()
        print 'writing file '+line[0]+'_smp_file.dat'
        out1 = open(line[0]+'smp_file.dat', 'w')
        well = line[0]

    if len(line) == 4:
        print >> out1, line[0]+'\t'+line[1]+' '+line[2]+'\t'+line[3]
    elif len(line) == 5:
        print >> out1, line[0]+'\t'+line[1]+' '+line[2]+'\t'+line[3]+' '+line[4]
    else:
        print 'length of line not expected'

out1.close()
