#!/usr/bin/python

primes = [i.strip() for i in open("primes").readlines()]

n = 0
total = 0
for prime in primes:
    print prime
    s = str(prime)
    ok = True
    for direction in range(2):
        for i in range(1, len(s)):
            if (direction == 0):
                sub = s[:i]
            else:
                sub = s[i:]
            if not sub in primes:
                ok = False
                break
        if ok == False:
            break
    if ok:
        print prime,
        if int(prime) > 9:
            n += 1
            print n
            total += int(prime)
        else:
            print
        if n >= 11:
            break

print total

