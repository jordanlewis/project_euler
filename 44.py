#!/usr/bin/python 

def gen_pentagonals():
    n = 1
    while True:
        yield n * ((3 * n) - 1) / 2
        n += 1

pentagonals = []
for x in gen_pentagonals():
    for pentagonal in pentagonals:
        if x + 
