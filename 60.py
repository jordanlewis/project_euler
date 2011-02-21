#!/usr/bin/python

import itertools

primes = [int(prime) for prime in open("primes")]
primes = primes[:1000]
print primes[-1]
primedict = dict([(prime, None) for prime in primes])


pairs = {}
for i in range(len(primes)):
    primei = primes[i]
    stri = str(primei)
    for j in range(i, len(primes)):
        primej = primes[j]
        strj = str(primej)

        if int(stri + strj) in primedict and int(strj + stri) in primedict:
            pairs[primei] = [primej] if primei not in pairs else pairs[primei] + [primej]
            pairs[primej] = [primei] if primej not in pairs else pairs[primej] + [primei]

newpairs = []
for i in sorted(pairs.keys()):
    for j in pairs[i]:
        if j in pairs and len(pairs[i]) >= 2:
            newpairs.append((i,j))


print newpairs

