f = open('files\\27-1001b.txt')
n, m = map(int, f.readline().split())
doma = [-1]*(m+1)
for e in f.readlines():
    num, kolsem = map(int, e.split())
    doma[num] = kolsem
minrast = 999999999999999999999999999999999999
ans = 0
for mesto in range(1, m+1):
    sumrast = 0
    if doma[mesto] != -1:
        continue
    for rasste in range(1, m+1):
        if doma[rasste] != -1:
            sumrast += (abs(mesto - rasste) * doma[rasste])
    if sumrast <= minrast:
        minrast = sumrast
        ans = mesto
print(ans)