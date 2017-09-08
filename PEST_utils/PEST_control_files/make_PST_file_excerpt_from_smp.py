# -*- coding: utf-8 -*-
"""

script to write a portion of the observations section of a PEST control file
from an existing bore sample file containing times and observed values of 
head, drawdown or some other time-varying "state variable"

this is for transient simulations that are included in a model calibration
it is assumed that observations related to only one location are in the 
input bore sample file

arguments that can be given on the command line (note - in order to supply a 
given argument, the previous ones have to be given as well):
 - name of the bore sample file
 - observation group name (OBGNME)
 - weight (applied uniformly across the group of observations)
 - starting number for observations - in case there may be others associated with the well already

this script can be executed in a Python GUI or from a batch file with 
the following command or similar:
python make_PST_file_excerpt_from_smp.py bob_obs.dat FHS_79 1.3 0

note that the limit on observation names for PEST ver. 14 is 20 characters, 
observation group names must be 12 characters or less in length

@author: djdahlstrom

"""

from string import upper, lower
import sys

# get bore sample file name
try:
    infile = sys.argv[1]
    print 'Opening file ', infile
    in1 = open(infile,'r')

except:
    print 'file name not given on command line, using default'
    infile = 'bob_obs.dat'
    in1 = open(infile,'r')

# get observation group name
try:
    OBGNME = sys.argv[2]
    print 'Observations are in group named ', OBGNME

except:
    print 'Group name not given on command line, using default'
    OBGNME = 'Bob'

# get observation weights
try:
    WEIGHT = sys.argv[3]
    print 'Observations given weight of ', WEIGHT

except:
    print 'Weight not given on command line, using default'
    WEIGHT = '1.5'

# get sequential number for first observation
try:
    obsno = int(sys.argv[4])
    print 'Starting number for observations ', obsno

except:
    print 'Initial observation number not supplied, use default of 1'
    obsno = 1

# read the bore sample file
contents = in1.readlines()
in1.close()

# create the instruction file
outfile = infile.replace('.dat', '_PST_part.dat')
print 'creating file '+outfile
ins1 = open(outfile, 'w')

# create an observation label file for use in Grapher or similar software
label_file = infile.replace('.dat', '_labels.dat')
outfile2 = open(label_file, 'w')
print 'creating file '+label_file

# changing to work with either Grapher-compatible or not; should screen for illegal characters
well = upper(contents[0].split()[0])

for i in contents:
    # changing to work with either Grapher-compatible or not
    line = i.split()
    OBSNME = well+'_'+str(obsno)
    print >> ins1, OBSNME+' '+line[-1]+' '+WEIGHT+' '+OBGNME
    # printing observation labels - make compatible with either Grapher-compatible or not
    if len(line) == 3:
        print >> outfile2, line[1]+'\t'+line[2]+'\t'+OBSNME
    elif len(line) == 4:
        print >> outfile2, line[1]+' '+line[2]+'\t'+line[3]+'\t'+OBSNME
    else:
        print 'unexpected length of line in bore sample file'
    # increment the observation counter
    obsno += 1

ins1.close()
outfile2.close()
