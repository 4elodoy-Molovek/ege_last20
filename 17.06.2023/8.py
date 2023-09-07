from itertools import product
alf = sorted('ДЕЙНПТЬЯ')
arr = [''.join(e) for e in product(alf, repeat=4)]
k = 0
for e in arr:
    k += 1
    print(k, e)