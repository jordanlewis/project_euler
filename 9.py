#!/usr/bin/python 

m = 2
n = 1
a = b = c = 0

while a + b + c != 1000:
    if m == n:
        m += 1
        n = 1
    else:
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        n+=1

print(a*b*c)
