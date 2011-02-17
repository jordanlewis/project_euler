def divisors(n):
    for i in xrange(1, n/2+1):
        if n%i == 0:
            yield i

abun = []

n = 28123

for i in range(1,n):
    tot = sum(divisors(i))
    if tot > i:
        print i
        abun.append(i)

print "whew, we got " + str(len(abun))

sums = set()
count = 0

for i in range(len(abun)):
    for j in range(i, len(abun)):
        count += 1
        s = abun[i] + abun[j]
        if not count % 10000:
            print count
        if s > n:
            break
        sums.add(s)

complement = set(range(n))

print complement
print sums

print sum(complement.difference(sums))
