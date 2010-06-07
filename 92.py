#!/usr/bin/python

total = 0

array = list(0 for i in range(568))
array[89] = 89
array[1] = 1

for i in range(1, 10000000):
    if not i % 10000:
        print i
    cur = [i]
    num = i
    while True:
        if num < 568 and array[num]:
            for j in cur:
                if (j < 568):
                    array[j] = array[num]
            if array[num] == 89:
                total += 1
        else:
            num = sum([int(i) ** 2 for i in str(num)])
            continue
        break


print total
