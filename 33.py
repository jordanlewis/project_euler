#!/usr/bin/python

found = 0
top = 0
bot = 1

fracs = []

def inc():
    global top, bot
    top += 1
    if top == bot:
        bot += 1
        top = 0


while found < 4:
    frac = float(top) / float(bot)
    strtop = str(top)
    strbot = str(bot)

    if top < 10 or bot < 10:
        inc()
        continue

    for pos in range(len(strtop)):
        digit = strtop[pos]
        if digit != '0':
            idx = strbot.find(digit)
            if idx == -1:
                continue

            newtop = float(strtop[:pos] + strtop[pos + 1:])
            newbot = float(strbot[:idx] + strbot[idx + 1:])
            if newbot != 0 and newtop / newbot == frac:
                fracs.append((top, bot))
                print top, bot, frac
                found += 1

    inc()

pairs = zip(*fracs)
print pairs
topproduct = reduce(lambda x,y: x*y,pairs[0])
botproduct = reduce(lambda x,y: x*y,pairs[1])
print "%d / %d" % (topproduct, botproduct)

print 1 / (float(topproduct)/botproduct)
