#!/usr/bin/python 

# This is in squares - we index from 0 because the # of nodes is 1 more than
# the number of squares
grid_size = 1

def num_routes(x, y):
    if y == grid_size or x == grid_size:
        return 1
    elif grid_size == x + 1:
        return (grid_size - y) + 1
    elif grid_size == y + 1:
        return (grid_size - x) + 1

print num_routes(0,0)
