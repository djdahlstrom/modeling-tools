# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 12:32:07 2013

script to convert an ASCII table into a .JML file for 
importing into OpenJUMP

assumes the file has a header line with names for the attribute fields

also assumes x coordinate is in 2nd column and y coordinate is in 3rd column

columns:
name
x
y
other attributes

@author: djdahlstrom

"""

import sys

try:
    in_name = sys.argv[1]
    print 'converting '+in_name+' to a python list'
    print 'makes lists of strings, not integers or floats'

except:
    in_name = 'digitized.dat'
    print 'file name not given on command line, assuming it is '+in_name
    print 'converting '+in_name+' to a jml file'

in1 = open(in_name, 'r')
contents = in1.readlines()
in1.close()

root = in_name.split('.')[0]

out1 = open(root+'.jml', 'w')
print >> out1, "<?xml version='1.0' encoding='UTF-8'?>"
print >> out1, '<JCSDataFile xmlns:gml="http://www.opengis.net/gml" xmlns:xsi="http://www.w3.org/2000/10/XMLSchema-instance" >'
print >> out1, '<JCSGMLInputTemplate>'
print >> out1, '<CollectionElement>featureCollection</CollectionElement>'
print >> out1, '<FeatureElement>feature</FeatureElement>'
print >> out1, '<GeometryElement>geometry</GeometryElement>'
print >> out1, '<ColumnDefinitions>'

# make a list of the field names (become attributes of features)
fields = []

# process header line
for i in contents[0:1]:
    line = i.split()
    for j in line[0:1]:
        print >> out1, r'     <column>'
        print >> out1, r'          <name>'+j+'</name>'
        print >> out1, r'          <type>STRING</type>'
        print >> out1, r'          <valueElement elementName="property" attributeName="name" attributeValue="'+j+'"/>'
        print >> out1, r'          <valueLocation position="body"/>'
        print >> out1, r'     </column>'
        fields.append(j)
    for j in line[3:]:
        print >> out1, r'     <column>'
        print >> out1, r'          <name>'+j+'</name>'
        print >> out1, r'          <type>STRING</type>'
        print >> out1, r'          <valueElement elementName="property" attributeName="name" attributeValue="'+j+'"/>'
        print >> out1, r'          <valueLocation position="body"/>'
        print >> out1, r'     </column>'
        fields.append(j)

print >> out1, r'</ColumnDefinitions>'
print >> out1, r'</JCSGMLInputTemplate>'
print >> out1, '\n'

# process rest of lines:
print >> out1, r'<featureCollection>'

for i in contents[1:]:
    # indext for lits of field names
    count = 0
    line = i.split()
    print >> out1, '     <feature>'
    print >> out1, '          <geometry>'
    print >> out1, '                <gml:Point>'
    print >> out1, '                  <gml:coordinates>'+line[1]+','+line[2]+' </gml:coordinates>'
    print >> out1, '                </gml:Point>'
    print >> out1, '          </geometry>'
    for j in line[0:1]:
        print >> out1, '          <property name="'+fields[count]+'">'+j+'</property>'
        count += 1
    for j in line[3:]:
        print >> out1, '          <property name="'+fields[count]+'">'+j+'</property>'
        count += 1
    print >> out1, '     </feature>'

print >> out1, r'     </featureCollection>'
print >> out1, r'</JCSDataFile>'
out1.close()
