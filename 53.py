#!/usr/bin/python 

def gen_fib_triangle(n):
    nValues = 0
    triangle = [range(x) for x in range(1,n+1)]
    triangle[0][0] = 1
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            total = 0
            if j > 0:
                total += triangle[i-1][j-1]
            if j < i:
                total += triangle[i-1][j]

            triangle[i][j] = total
            if total > 1000000:
                nValues += 1

    print nValues
    return triangle

gen_fib_triangle(101)
