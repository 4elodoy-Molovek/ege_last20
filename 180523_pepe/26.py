f = open('files\\26.txt')
k = int(f.readline())
n = int(f.readline())
pas = []
kam = [0] * k
kol = n
zan = []
odz = 0
for e in f.readlines():
    prib, th = map(int, e.split())
    pas.append([prib, th + prib, th])
pas.sort()

for cur_pas in pas:
    prib, otb, th = cur_pas[0], cur_pas[1], cur_pas[2]
    for i in range(k):
        if prib > kam[i]:
            kam[i] = otb
            kol -= 1
            zan.extend([prib + 1, -otb])
            break
zan.sort(key=abs)
an = []
kzk = 0
tmem = 0
for e in zan:
    if e > 0:
        kzk += 1
        if kzk == k:
            tmem = e
    if e < 0:
        if kzk == k:
            an.append((abs(e + tmem)))
        kzk -= 1
print(kol, sum(an))