#!/usr/bin/python 

maxproduct = 0
for a in range(100,999):
    for b in range(100,999):
        product = str(a * b)
        if len(product) % 2 == 0:
            if product[0:len(product)/2] == product[:len(product)/2-1:-1]:
                if int(product) > maxproduct:
                    print product
                    maxproduct = int(product)
        else:
            if product[0:len(product)/2] == product[:len(product)/2:-1]:
                if int(product) > maxproduct:
                    print product
                    maxproduct = int(product)
