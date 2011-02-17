primelist = [int(x.strip()) for x in open('primes').readlines()]

primes = [0 for x in range(1000000)]
for i in primelist:
    primes[i] = 1

maxSeq = 0
seq = 0
bestA = 0
bestB = 0

for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0

        while primes[n**2 + a * n + b] != 0:
            n += 1

        if n > maxSeq:
            print "new max: %d at (%d, %d)" % (n, a, b)
            maxSeq = n
            bestA = a
            bestB = b

print bestA * bestB
