#!/usr/bin/python 

def rotations(x):
    x = [l for l in str(x)]
    for _ in xrange(len(x) - 1):
        x.append(x.pop(0))
        yield "".join(x)



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
    if not all([(int(i) % 2) for i in str(prime)]):
        continue
    circular = True
    for num in rotations(prime):
        if num not in primes:
            circular = False
            break
    if circular:
        print prime
        circulars.append(prime)

print len(circulars)

