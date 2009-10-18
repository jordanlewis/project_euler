#!/usr/bin/python 

size = 15
triangle = [[0 for x in xrange(y)] for y in xrange(1, size + 1)]

filename = "18.dat"
file = open(filename)

line_num = 0
for line in file.readlines():
    pos_num = 0
    for num in line.split(" "):
        triangle[line_num][pos_num] = int(num)
        pos_num += 1
    line_num += 1

file.close()

assert line_num == pos_num
assert line_num == size

for row in reversed(xrange(1, line_num)):
    for pos in xrange(row):
        triangle[row-1][pos] += max(triangle[row][pos], triangle[row][pos+1])

print triangle[0][0]

