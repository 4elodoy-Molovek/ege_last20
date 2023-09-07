from itertools import product as prod

arr = [''.join(e) for e in prod('0NCNCNCNCNC', repeat=6) if e[0] != '0']
chet = '02468A'
nechet = '13579'
kol = 0

for e in arr:
    if not('NNN' in e):
        kol += 1

print(kol)
