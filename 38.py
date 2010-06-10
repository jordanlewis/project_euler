best = 0
for i in range(9999):
    size = 0
    num = ""
    n = 1
    while size < 9:
        sub = str(i * n)
        size += len(sub)
        num += sub
        n += 1
    if size > 9:
        continue

    dict = {}
    pan = True
    for c in num:
        if c == "0" or dict.has_key(c):
            pan = False
            break
        dict[c] = 1
    if pan:
        if int(num) > best:
            print "new best: " + num
            best = int(num)

print best
