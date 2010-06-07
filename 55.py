#!/usr/bin/python

def palindrome(str):
    l = len(str)
    a = l / 2
    b = a
    if not l % 2:
        # odd number of digits
        b -= 1
    if str[:a] == str[:b:-1]:
        return True
    else:
        return False

nlych = 0
for i in range(10000):
    num = i
    palin = False
    for j in range(50):
        num += int("".join(reversed(str(num))))
        if palindrome(str(num)):
            palin = True
            break
    if not palin:
        print i,j,num
        nlych += 1

print nlych
