#!/usr/bin/python

x = 1
while True:
    bad = True
    lst = sorted(list(str(x)))
    for i in range(2, 7):
        if not lst == sorted(list(str(i * x))):
            break
    if i == 6:
        break
    x += 1

print x

