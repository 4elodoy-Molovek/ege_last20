from itertools import product as prod

arr = [''.join(e) for e in prod('АКЛМНЯ', repeat=5)]

n = 0
for e in arr:
    n += 1
    print(n, e)
