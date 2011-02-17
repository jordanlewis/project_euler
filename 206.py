import math

target = "1x2x3x4x5x6x7x8x9x0"


start = "1xxxxxxx30"

def go():
        i = 100000
        while i < 999999:
            for b in ("3", "7"):
                s = "13" + str(i) + b + "0"
                r = str(int(s) ** 2)
                if not i % 100000:
                    print s, r
                fail = False
                for k in range(19):
                    if target[k] != "x" and target[k] != r[k]:
                        fail = True
                        break
                if fail:
                    i += 1
                    continue
                else:
                    print s
                    print "                 " + r
                    return


s = "11223344556677889900"
fail = False
for k in range(19):
    if target[k] != "x" and target[k] != s[k]:
        fail = True
        break
print fail
go()
