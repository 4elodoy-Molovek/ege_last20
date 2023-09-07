f = open('files\\27B_7691.txt')
n, m = map(int, f.readline().split())
arr = [-1] * m
for e in f.readlines():
    num, sem = map(int, e.split())
    arr[num] = sem

mns = 99999999999999999999999999999999999999999999999999999999999999999
mn = 0
rs, rf, ls, lf = 0, 0, 0, 0
for i in range(m):
    if arr[i] != -1:
        rs += i*arr[i]
        rf += arr[i]

for i in range(1, m):
    rs -= rf
    ls += lf
    if arr[i] != -1:
        rf -= arr[i]
        lf += arr[i]
    ts = rs + ls
    if ts <= mns and arr[i] == -1:
        mns = ts
        mn = i
print(mn)
