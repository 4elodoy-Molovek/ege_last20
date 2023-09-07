f = open('files\\17-2002.txt')
arr = [int(e) for e in f.read().split()]


mx2 = 0
for e in arr:
    if str(e)[-1] == '2':
        mx2 = max(mx2, e)

kol = 0
mxf = 0
for e in arr:
    if e % 3 == 0:
        if e % 7 != 0 and e % 17 != 0:
            if mx2 % e == 0:
                kol += 1
                mxf = max(e, mxf)

print(kol, mxf)
