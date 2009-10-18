#!/usr/bin/python 
from math import sqrt
import traceback
import psyco

psyco.full()

d_chart = {}
amicable_pairs = []

def get_divisors(num, proper=False):
    divs = []
    for possible_divisor in range(1, int(sqrt(num))):#, 1, -1):
        if num % possible_divisor == 0:
            divs.append(possible_divisor)
            if not proper or possible_divisor != 1:
                divs.append(num / possible_divisor)
    return divs

for i in range(1, 10000):
    d_chart[i] = sum(get_divisors(i, proper=True))

for key, value in d_chart.items():
    if key == d_chart.get(value):
        if key != value:
            amicable_pairs.append(key)

print amicable_pairs
print sum(amicable_pairs)
