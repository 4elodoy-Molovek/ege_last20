from itertools import product

arr = sorted([''.join(e) for e in product('ВИНОГРАД', repeat=4)])
print(arr.index('ГОАА') + 1)
