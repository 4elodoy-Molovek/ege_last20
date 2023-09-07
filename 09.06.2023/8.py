from itertools import product as prod
alf = 'ЕПСУХ'
sogl = 'ПСХ'
arr = [''.join(e) for e in prod(alf, repeat=5) if e[-1] in sogl]
n = 0
for e in arr:
    n += 1
    print(e, n)