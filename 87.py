#!/usr/bin/python

primes = [int(x) for x in open('primes').readlines()]
sums = {}

for i in primes:
    sq = i ** 2
    if sq >= 50000000:
        break
    for j in primes:
        cu = j ** 3
        sqcu = sq + cu
        if sqcu >= 50000000:
            break
        for k in primes:
            fo = k ** 4
            sqcufo = sqcu + fo
            if sqcufo >= 50000000:
                break
            sums[sqcufo] = True


print len(sums)
