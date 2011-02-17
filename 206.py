#!/usr/bin/python 

for i in xrange(1010100000, 3162277662):
    s = str(i ** 2)
    if not i % 10000:
        print i, s
    found = True
    for j in range(9):
        if int(s[j * 2]) != (j + 1):
            found = False
            break
    if found:
        print i, s
        break
    


#left = 1000000000
#right = 3162277662
#dir = 0
#while True:
#    i = left + (right - left) / 2
#    s = str(i ** 2)
#    print s
#    for j in range(9):
#        dir = int(s[j * 2]) - (j + 1)
#        if (dir != 0):
#            break
#    if j == 8:
#        print s
#        break
#    print j, dir, left, right
#    if (dir < 0):
#        left = i
#    elif (dir > 0):
#        right = i
