f = open('files\\17_5292.txt')
arr = [int(e) for e in f.read().split()]

mn123 = 99999999
for e in arr:
    if e % 123 == 0:
        mn123 = min(mn123, e)

mxs = 0
kol = 0
for i in range(1, len(arr)):
    t1, t2 = arr[i - 1], arr[i]
    if (t1 % 2023 >= mn123 > t2 % 2023) or (t2 % 2023 >= mn123 > t1 % 2023):
        kol += 1
        ts = t1 + t2
        mxs = max(ts, mxs)
print( kol, mxs)
