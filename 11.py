#!/usr/bin/python 

filename = "11.dat"

file = open(filename)

array = [[0 for y in xrange(20)] for x in xrange(20)]
line_num = 0
col_num = 0
for line in file.readlines():
    col_num = 0
    for number in line.split():
        array[col_num][line_num] = int(number)
        col_num += 1
    line_num += 1

file.close()

maxprod = 0
for y in xrange(20):
    for x in xrange(20):
        for xmod, ymod in [(1, 0), (0, 1), (1, 1), (-1, 1)]:
            prod = array[x][y]
            curx, cury = x, y
            for _ in xrange(3): # 3 times
                curx += xmod
                cury += ymod
                if curx >= 0 and curx < 20 and cury >= 0 and cury < 20:
                    prod *= array[curx][cury]
                    if prod > maxprod:
                        maxprod = prod
                        print x, y
                        print prod
                else:
                    break



