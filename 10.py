#!/usr/bin/python 

pfile = open("primes", "r")

sum = 0
for line in pfile.readlines():
    sum += int(line)
pfile.close()

print sum
