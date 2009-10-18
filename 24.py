#!/usr/bin/python

import psyco
psyco.full()

def perm(lst):
    if lst:
        return [[x] + ps for x in lst for ps in perm([e for e in lst if e!=x])]
    else:
        return [[]]

print perm(range(10))
#perms = [int("".join([str(i) for i in pl])) for pl in perm(range(10))]
#perms.sort()
#print perms[1000000]
