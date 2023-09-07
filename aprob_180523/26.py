f = open('files\\26_8512.txt')

k = int(f.readline())
n = int(f.readline())
arr = []
kol = 0
last_used = 0
last_used_time = 0
kameri = [0] * k
for e in f.readlines():
    prib, otb = map(int, e.split())
    arr.append([prib, otb + 1])
arr.sort()

for klient in arr:
    for i in range(k):
        if klient[0] >= kameri[i]:
            kameri[i] = klient[1]
            kol += 1
            if last_used_time == klient[0]:
                last_used = min(last_used, i+1)
            else:
                last_used = i + 1
                last_used_time = klient[0]
            break
print(kol, last_used)
