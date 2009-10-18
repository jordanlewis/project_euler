#!/usr/bin/python 

letters = [x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
letters = dict(zip(letters, range(1,27)))
print letters

namefile = open("22.dat", "r")

names = [line.rstrip("\n") for line in namefile.readlines()]
namefile.close()
names.sort()

def namevalue(name):
    return reduce(lambda x,y:x+y, [letters[x] for x in name])

totalscore = 0

for i in range(len(names)):
    totalscore += (i+1) * namevalue(names[i])
print totalscore

