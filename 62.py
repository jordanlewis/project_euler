#!/usr/bin/python 

import itertools

cubes = {}
for i in range(10000):
    cubes[str(i)] = str(i ** 3)

cuberoots = dict.fromkeys(cubes.values(), cubes.keys())

cuberootslen = [{} for i in range(100)]
for cube, n in cuberoots.items():
    cuberootslen[len(cube)][cube] = n


print "done generating cubes"

for n, cube in cubes.items():
    nperms = 0
    digits = [digit for digit in cube]
    cubelen = len(cube)
    sortedcube = sorted(cube)
    for x in cuberootslen[cubelen].keys():
        if sorted(x) == sortedcube:
            nperms += 1
        s = sorted(x)

    #for permutation in set(itertools.permutations(digits)):
        #if "".join(permutation) in cuberootslen[cubelen]:
            #nperms += 1
    if nperms > 2:
        print n, cube, nperms
    else:
        cuberoots.pop(cube)
    if nperms == 5:
        print "omg", n, cube, nperms

