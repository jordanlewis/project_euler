#!/usr/bin/python 

import math
phi = long((1+math.sqrt(5))/2)

def fib(n):
    n = long(n)
    return (phi**n - (1 - phi)**n)/math.sqrt(5)

term = 0
n = 1
print fib(1500)
while len(str(term)) < 1000:
    term = fib(n)
    n+=1
print n, term


