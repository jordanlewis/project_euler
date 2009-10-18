#!/usr/bin/python 

def collatz(n):
    yield n
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n) + 1
        yield n

#for x in collatz(13):
#    print x
#print [x for x in collatz(13)]

maxlen = curlen = 0
for n in xrange(1,1000000):
#    print [x for x in collatz(n)]
    curlen = len([x for x in collatz(n)])
    if curlen > maxlen:
        maxlen = curlen
        print(str(n) + ": " + str(maxlen))

print maxlen
    
