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

sum = 0
for i in range(1000000):
    if palindrome(str(i)) and palindrome(bin(i)[2:]):
        sum += i

print sum
