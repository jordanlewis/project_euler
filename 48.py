#!/usr/bin/python 

sum = 0
for n in range(1,1001):
    sum += long(n**n)
print n

print sum
print str(sum)[-10:]

