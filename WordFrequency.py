
import csv

infile = open('sometext.txt','r')

vals = {}

for v in infile:
     
    for c in v.split():
        vals[c] = v.count(c)

for word in vals:
    print(word + " has a frequency of " + str(vals[word]))
