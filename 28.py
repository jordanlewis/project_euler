#!/usr/bin/python 


size = 1001
spiral = list(0 for i in range(size * size))

idx = size * (size/2) + size/2

# 0 = right, 1 = down, 2 = left, 3 = up

diroffsets = [1, size, -1, -size]

num = 1
dir = 0
spiral[idx] = num
num += 1
idx += 1
spiral[idx] = num
num += 1
dir = 1
while idx != size - 1:
    nextdir = (dir + 1) % 4
    if spiral[idx + diroffsets[nextdir]] == 0:
        dir = nextdir
    idx += diroffsets[dir]
    spiral[idx] = num
    num += 1

total = -1 # 1 will get counted twice
for i in range(size):
    total += spiral[i * size + i]
    total += spiral[i * size + (size - i - 1)]

print total

