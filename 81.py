#!/usr/bin/python

matrix = []

for line in open("81.dat").readlines():
    matrix.append([int(x) for x in line.split(',')])

dp = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == 0 and j == 0:
            best = 0
        elif i == 0:
            best = dp[i][j - 1]
        elif j == 0:
            best = dp[i - 1][j]
        else:
            best = min(dp[i][j - 1], dp[i - 1][j])

        dp[i][j] = best + matrix[i][j]

print dp[len(matrix) - 1][len(matrix) - 1]

