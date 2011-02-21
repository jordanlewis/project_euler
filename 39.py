#!/usr/bin/python

import math

triples = dict([(i, 0) for i in range(1001)])

for i in range(1, 1001):
    for j in range(1, 1001):
        hyp = math.sqrt(float(i) ** 2 + float(j) ** 2)
        if hyp % 1 == 0:
            hyp = int(hyp)
            perimeter = i + j + hyp
            if perimeter <= 1000:
                triples[perimeter] += 1

maxtriples = 0
maxperimeter = 0
for perimeter, ntriples in triples.items():
    if ntriples > maxtriples:
        maxtriples = ntriples
        maxperimeter = perimeter

print maxtriples, maxperimeter
