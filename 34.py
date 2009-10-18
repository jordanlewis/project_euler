#!/usr/bin/python 

def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x-1)

factorials = [factorial(x) for x in xrange(10)]

fsum = 0
for x in xrange(3,factorials[9] + 1):
    if sum([factorials[int(d)] for d in str(x)]) == x:
        fsum += x
        print x

print fsum
