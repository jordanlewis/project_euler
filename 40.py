#!/usr/bin/python


s = ""
for i in range(1000000):
    s = s + str(i)

print reduce(lambda x, y: x*y, [int(s[10 ** i]) for i in range(7)])
