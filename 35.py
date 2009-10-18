#!/usr/bin/python 

def rotations(x):
    x = [l for l in str(x)]
    for _ in xrange(len(x) - 1):
        x.append(x.pop(0))
        yield int("".join(x))



primefilename = "primes"
primefile = open(primefilename)

primes = []
for prime in primefile.readlines():
    primes.append(prime[:-1])

primefile.close()

x = 123456
for r in rotations(x):
    print r
circulars = []
for prime in primes:
    circular = 1
    for num in rotations(prime):
        if num not in primes:
            circular = 0
            break
    if circular:
        print prime
        circulars.append(prime)

print len(circulars)

