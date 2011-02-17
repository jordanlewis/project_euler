#!/usr/bin/python

primes = [2,3,5,7,11,13,17]
products = [[] for prime in primes]
postfixes = [{} for prime in primes]
for i in range(len(primes)):
    prime = primes[i]
    multiplier = 1
    product = 1
    while product < 1000:
        product = multiplier * prime
        multiplier += 1
        product_str = ("%3d" % product).replace(" ", "0")
        if product_str[0] == product_str[1] or \
           product_str[0] == product_str[2] or \
           product_str[1] == product_str[2]:
            continue

        prefix = product_str[:2]
        if i == 0 or prefix in postfixes[i-1]:
            if i > 0:
                digitsbefore = [a[0] for a in postfixes[i - 1][prefix]]
                for digit in digitsbefore:
                    if digit in product_str:
                        continue

            products[i].append(product_str)
            postfix = product_str[1:]
            if postfix in postfixes[i]:
                postfixes[i][postfix].append(product_str)
            else:
                postfixes[i][postfix] = [product_str]

sum = 0
def gen_pandigitals(ndigit, digitsleft, postfix):
    if ndigit == 1:
        for digit in digitsleft:
            if digit not in postfix:
                print "found " + digit + postfix
                global sum
                sum += int(digit + postfix)
                return
        assert(False)


    for triplet in products[ndigit - 2]:
        if postfix and triplet[1:] != postfix[:2]:
            continue
        valid = True
        for digit in triplet:
            if digit not in digitsleft:
                valid = False
                break
        if not valid:
            continue

        newdigitsleft = digitsleft.copy()
        newdigitsleft.remove(triplet[2])

        if not postfix:
            newpostfix = triplet
        else:
            newpostfix = triplet[0] + postfix

        gen_pandigitals(ndigit - 1, newdigitsleft, newpostfix)

gen_pandigitals(8, set([str(x) for x in range(10)]), "")
print sum
