n = 1
sumofsquares = 0
sum = 0

while n <= 100:
    sum += n
    sumofsquares += (n * n)
    n += 1

squareofsum = sum * sum

print "sum of squares:" + str(sumofsquares)
print "square of sum:" + str(squareofsum)

print squareofsum - sumofsquares
