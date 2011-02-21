#!/usr/bin/python
import itertools



nways = 0
for i in itertools.permutations(range(100)):
    print i
    if sum(i) == 100:
        nways += 1
print nways
