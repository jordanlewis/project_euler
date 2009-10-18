#!/usr/bin/python 

file = open("13.dat", "r")

s = 0
for line in file.readlines():
    s += int(line)

file.close()


print str(s)[0:10]
    
