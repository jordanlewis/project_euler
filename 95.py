#!/usr/bin/python
import math

max = 1000000
sieve = dict([(i, []) for i in range(max)])
for i in range(1, max):
    for j in range(i * 2, max, i):
        sieve[j].append(i)

sums = dict([(i, sum(sieve[i])) for i in range(max)])

bestchain = []
for i in range(1,max):
    chain = []
    curelem = i
    while curelem not in chain:
        if curelem > max:
            break
        chain.append(curelem)
        curelem = sums[curelem]
    if curelem == chain[0]:
        if len(chain) > len(bestchain):
            bestchain = chain

print min(bestchain)
