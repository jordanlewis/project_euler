#!/usr/bin/python 

found = {}

initdigits = dict([(i, False) for i in range(1,10)])

for i in range(999):
    stri = str(i)
    if '0' in stri:
        continue

    repeats = False
    digits = {}
    for letter in stri:
        if letter in digits:
            repeats = True
            break
        digits[letter] = True
    if repeats:
        continue

    lenstri = len(stri)
    for j in range(9999):
        strj = str(j)
        if '0' in strj:
            continue
        product = i * j
        if product % 10 == 0:
            continue
        strproduct = str(product)
        if '0' in strproduct:
            continue
        strjandproduct = strj + strproduct
        sumstr = stri + strjandproduct
        if lenstri + len(strjandproduct) != 9:
            continue
        digits = initdigits.copy()
        fail = False
        for k in sumstr:
            if k in digits:
                fail = True
                break
            else:
                digits[k] = True

        if fail:
            continue

        print "%d * %d = %d" % (i, j, product)
        found[product] = True


print sum(found.keys())
