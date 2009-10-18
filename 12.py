#!/usr/bin/python 
from math import sqrt
import traceback
import psyco

psyco.full()

saved_divisors = {}
def get_divisors(num):
    divs = []
    for possible_divisor in range(1, int(sqrt(num))):#, 1, -1):
        if sum % possible_divisor == 0:
            divs.append(possible_divisor)
            divs.append(sum / possible_divisor)
    return divs

sum = 0
n = 1
maxdivs = 0

while True:
    sum += n
    divs = get_divisors(sum)
    num_divs = len(divs)
    if num_divs > maxdivs:
        maxdivs = num_divs
        print maxdivs, sum
    if num_divs > 500:
        print sum
        break
    n += 1
