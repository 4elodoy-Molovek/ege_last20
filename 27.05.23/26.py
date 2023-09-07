import math

f = open('files\\26_8380.txt')

K, N = map(int, f.readline().split())
time = []
for line in f.readlines():
    a, b = map(int, line.split())
    time.append(a)
    time.append(-b)
time.sort(key=abs)
# print(time)
kh = 0
mkh = 0
last = 0
for t in time:
    if t > 0:
        kh += 1
        if kh > mkh:
            mkh = kh
        last = kh
    else:
        kh -= 1
print(math.ceil(mkh / K), last)
