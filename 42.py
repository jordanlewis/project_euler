#!/usr/bin/python 

trinums = [sum(xrange(i)) for i in xrange(1,100)]
let = [x for x in "abcdefghijklmnopqrstuvwxyz"]
let2num = dict([(let[i], i+1) for i in xrange(26)])
print let2num

filename = "42.dat"
file = open(filename)
line = file.readline()

line = line.replace('"','')

triwords = 0
for word in line.split(','):
    if sum(let2num[x.lower()] for x in word) in trinums:
        triwords += 1
        print word

print triwords
