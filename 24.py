#!/usr/bin/python

def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n - 1)

def nth_permutation(init, n):
    nelts = len(init)
    if nelts == 1:
        return init

    div = 0
    nperms = factorial(nelts - 1)
    rem = n
    if nperms < n:
        div = n / nperms
        rem = n - div * nperms
        if rem == 0:
            div -= 1
            rem -= nperms

    print n, init, nelts, init[div]

    return init[div] + nth_permutation(init[:div] + init[div+1:], rem)


target = 1000000
initial = "0123456789"

print nth_permutation(initial, target)
