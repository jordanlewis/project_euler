#!/usr/bin/python 

primes = [int(prime) for prime in open("primes").readlines()]
primedict = dict([(int(prime), True) for prime in primes])

nprimes = len(primes)
maxprime = 0
for i in range(nprimes):
    sum = 0
    nums = []
    for j in range(i, nprimes):
        sum += primes[j]
        nums.append(primes[j])
        if sum in primedict:
            if sum > maxprime:
                maxprime = sum
                print nums
                print maxprime

print maxprime
