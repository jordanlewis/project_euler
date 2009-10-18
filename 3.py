#!/usr/bin/python 

import math
phi = (1+math.sqrt(5))/2

def fib():
    a, b = 0, 1
    while b < 1000000:
        if b % 2 == 0:
            yield b
        a, b = b, a+b

print reduce(lambda x, y: x+y, [x for x in fib()])
