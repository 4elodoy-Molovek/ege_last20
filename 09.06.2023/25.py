from fnmatch import fnmatch as fn


def SumDel(x):
    sum = 0
    for i in range(1, int(x ** 0.5)+1):
        if x % i == 0:
            sum += i
            sum += (x // i)
    return sum


for i in range(500_000, 1_000_000):
    if fn(str(SumDel(i)), '*7?'):
        print(i, SumDel(i))

