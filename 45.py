def hexagonals():
    n = 1
    while True:
        yield n * (2*n - 1)
        n += 1

def pentagonals():
    n = 1
    while True:
        yield n * (3 * n  - 1) / 2
        n += 1

def triangles():
    n = 1
    while True:
        yield n * (n + 1) / 2
        n += 1

tri = triangles()
pen = pentagonals()
hex = hexagonals()

ntri = tri.next()
npen = pen.next()
nhex = hex.next()

while True:
    nhex = hex.next()
    while npen < nhex:
        npen = pen.next()
    while ntri < nhex:
        ntri = tri.next()

    if nhex == npen and nhex == ntri:
        print nhex
