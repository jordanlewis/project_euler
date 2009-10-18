#!/usr/bin/python

n = 1
sum = 0
while n < 1000:
    if n % 3 == 0:
        sum += n
    elif n % 5 == 0:
        sum += n
    n+=1

print sum
