#!/usr/bin/python 

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

f = factorial(100)

print reduce(lambda x, y: x+y, [int(x) for x in str(f)])

