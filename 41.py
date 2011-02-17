primelist = [int(x.strip()) for x in open('primes').readlines()]

primes = [0 for x in range(1000000)]
for i in primelist:
    primes[i] = 1


for i in range(1000000):
    if primes[i]:
        dict = {}
        pan = True
        for c in str(i):
            if dict.has_key(c):
                pan = False
                break
            dict[c] = 1
        if pan:
            print i
