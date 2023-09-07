from fnmatch import fnmatch as fn


def SumCif(x):
    ss = 0
    t = str(x)
    for e in t:
        ss += int(e)
    return ss


arr = []
for i in range(0, 10 ** 9, 2023):
    if fn(str(i), '20*23'):
        if SumCif(i) % 7 == 0 and SumCif(i) < 20:
            arr.append(i)
arr.sort()
for e in arr:
    print(e)


