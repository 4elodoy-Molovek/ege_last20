f = open('files\\17-1007.txt')
arr = [int(e) for e in f.readlines()]

Min2 = 999999999999999999999999999999999999999999999999
for e in arr:
    ts = str(abs(e))
    if len(ts) == 2:
        Min2 = min(Min2, e ** 2)

Kol = 0
Min_Sum = 9999999999999999999999999999999999999999999999
for i in range(1, len(arr)):
    t1, t2 = arr[i - 1], arr[i]
    if (t1 ** 2 < Min2) or (t2 ** 2 < Min2):
        if t1 + t2 >= 0:
            Kol += 1
            Min_Sum = min(Min_Sum, (t1 + t2))
print(Kol, Min_Sum)

