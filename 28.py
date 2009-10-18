#!/usr/bin/python 


diagnum = 1001
halfdiag = 3
topright = sum([(((2*x) + 1) ** 2) for x in xrange(halfdiag)])
botleft = sum([((x-1) * (2 ** x)) + 1 for x in xrange(halfdiag)]) - 1
`:


print topright + topleft + botright + botleft
