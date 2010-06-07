#!/usr/bin/python

best = 0
for i in range(100):
    for j in range(100):
        cur = sum([int(k) for k in str(i ** j)])
        if cur > best:
            best = cur

print best


