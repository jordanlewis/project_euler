#!/usr/bin/python 

sums = []
for n in xrange(2,1000000):
    dsum = sum([int(d) ** 5 for d in str(n)])
    if dsum == n:
        sums.append(dsum)
        print dsum

print sums
print sum(sums)
