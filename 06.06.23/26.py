f = open('files\\26-1003.txt')
n = int(f.readline())
k = int(f.readline())
pizdec = 1380
gosti = []
stoli = [0] * k
kol = 0
LastStol = 0
for e in f.readlines():
    nach, kon = map(int, e.split())
    T = kon - nach
    gosti.append([nach, T, kon])
gosti.sort()

for gost in gosti:
    ok = False
    for i in range(k):
        if gost[0] > stoli[i]:
            stoli[i] = gost[2] + 5
            ok = True
            kol += 1
            LastStol = i + 1
            break
    if not ok:
        MinTime = min(stoli) - gost[0] + 1
        MinStol = min(stoli)
        if MinTime <= 10:
            ind = stoli.index(MinStol)
            if stoli[ind] + 1 + gost[1] <= pizdec:
                stoli[ind] += 1 + gost[1] + 5
                kol += 1
                LastStol = ind + 1
print(kol, LastStol)
