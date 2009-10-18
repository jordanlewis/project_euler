
x = 20

n = x

n = 49008960

foo = 1


#while 1:
#    blorp = [n % x for x in xrange(2,



list = [3, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print list
while foo < x - 1:
    foo = 1
    for divisor in list:
        if n % divisor == 0:
            foo = divisor
        else:
            break
    if foo >= 17:
    
        print str(n) + ": " + str(foo)
    #print n
    n += x
print n - x
