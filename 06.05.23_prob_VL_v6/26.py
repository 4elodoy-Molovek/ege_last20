from math import ceil

f = open('files\\26-1003.txt')
n = int(f.readline())
k = int(f.readline())
c = int(f.readline())
arr = []
park = [[0]*k, [0]*k, [0]*k]
kol = 0
prib = 0
for e in f.readlines():
    nach, kon, lv = map(int, e.split())
    arr.append([nach, kon, lv])
arr.sort()

for client in arr:
    nach = client[0]
    kon = client[1]
    lv = client[2] - 1
    dlit = ceil((kon - nach) / 3600)
    for i in range(k):
        if park[lv][i] <= nach:
            park[lv][i] = kon + 60
            kol += 1
            if lv == 0:
                prib += c * dlit
            if lv == 1:
                prib += 2 * c * dlit
            if lv == 2:
                prib += 4 * c * dlit
            break
print(prib, kol)

