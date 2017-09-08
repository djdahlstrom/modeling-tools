# -*- coding: utf-8 -*-
"""

script to write transient observations instruction files
from an existing bore sample file

assuming at this point that it is a Grapher-compatible bore sample file
in which tabs separate well name from date/time from related value and that 
only one location is represented

the results can be checked using the PEST utility INSCHEK:
inschek bob_obs.dat.ins bob_obs.dat

@author: djdahlstrom

"""

from string import upper, lower
import sys

# get filename if supplied
try:
    infile = sys.argv[1]
    print 'Opening file ', infile
    in1 = open(infile,'r')

except:
    print 'file name not given on command line, using default'
    infile = 'bob_obs.dat'
    in1 = open(infile,'r')

# get initial observation nummber if supplied by user
try:
    obsno = int(sys.argv[2])
    print 'Initial observation number is ', obsno

except:
    print 'Initial observation number not supplied, use default of 1'
    obsno = 1

# read the bore sample file
contents = in1.readlines()
in1.close()

# create the instruction file
outfile = infile+'.ins'
print 'creating file '+outfile
ins1 = open(outfile, 'w')

# create an observation label file - note - this may have little value as the 
# modeled equivalents are of less interest than the measured values - a label
# file of the observations is made using script make_PST_file_excerpt_from_smp.py
outfile2 = open(infile.replace('.dat', '_labels.dat'), 'w')

print >> ins1, 'pif @'

well = upper(contents[0].split('\t')[0])
counter = 0

for i in contents:
    line = i.split('\t')
    counter += 1
    #label = lower(str2xl(toStr(counter,26)))
    print >> ins1, '@'+line[1]+'@ w !'+well+'_'+str(counter)+'!'
    print >> outfile2, line[1]+'\t'+line[2][0:-1]+'\t'+well+'_'+str(counter)

ins1.close()
outfile2.close()
   