from itertools import product
from itertools import permutations


def F(x, y, z):
    return (y <= z) and not (z and x)


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    tab = [(1, a1, a2),
           (a3, a4, a5),
           (1, a6, 1)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyz'):
            if [F(**dict(zip(p, r))) for r in tab] == [1, 1, 1]:
                print(*p, sep='')
