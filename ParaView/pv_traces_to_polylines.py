import shapefile

'''

script to convert saved traces from ParaView to polyline shapefiles

note - depending on whether vorticity is calculated, the number of
columns in the file exported from ParaView may vary

columns of interest are:
"IntegrationTime"
"Points:0"
"Points:1"

djdahlstrom

'''

import sys

try:
    in_name = sys.argv[1]
    print 'converting '+in_name+' to polyline shapefile'

except:
    in_name = 'bob.csv'
    print 'file name not given on command line, assuming it is bob.csv'
    print 'converting '+in_name+' to a shapefile'

in1 = open(in_name, 'r')
contents = in1.readlines()
in1.close()

root = in_name.split('.')[0]
#out1 = open(root+'.jml', 'w')

# process header
line = contents[0].split(',')
time = line.index('"IntegrationTime"')
x = line.index('"Points:0"')
y = line.index('"Points:1"')

# create blank particle dictionary
particle_dict = {}

# particle number, as an integer
particle = -1

for i in contents[1:]:
    line = i.split(',')
    # see if integration time reset
    if line[time] == '0':
        particle += 1
        particle_dict[particle] = [[float(line[x]), \
                                        float(line[y])]]
    else:
        particle_dict[particle].append([float(line[x]), \
                                        float(line[y])])

# sort the dictionary based on the particle numbers
keys = particle_dict.keys()
keys.sort()

# instantiate a shapefile
w = shapefile.Writer(shapefile.POLYLINE)
# add a field to the attribute table for the particle index number
# 'N' here is for number, integer not regconized as a field type
#  Types can be: Character, Numbers, Longs, Dates, or Memo. 
w.field('Particle','N',8)

for i in keys:
    w.line(parts=[particle_dict[i]])
    w.record(i)

w.save(root)
