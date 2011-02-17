#!/usr/bin/python
import math

i = 1000000000000

while True:
    d = i * (i - 1)
    h = d / 2
    s = math.sqrt(h)
    if math.floor(s) * math.ceil(s) == h:
        break
        print i
    print i, d, h, s
    i += 1
