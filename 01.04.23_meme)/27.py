from math import ceil

f = open('files\\27-123b.txt')

N, K, V = map(int, f.readline().split())

arr = []
for e in f.readlines():
    t1, t2 = map(int, e.split())
    t2p = ceil((t2 / V))
    arr.append([t1, t2p])

stoim = 0
mst = 999999999999999999999999999999999999999999999999999999999999999999999
for i in range(0, len(arr)):
    for j in range(0, len(arr)):
        rast1 = abs(arr[j][0] - arr[i][0])
        rast2 = abs(K - rast1)
        stoim += min(rast2, rast1)*arr[j][1]
    if mst > stoim:
        mst = stoim
        print(mst, i)
    stoim = 0
