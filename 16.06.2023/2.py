from itertools import permutations
from itertools import product


def F(x, y, z, w):
    return ((w <= y) <= (x == y)) or (not z)


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    tab = [(a1, 0, 1, 0),
           (0, a2, a3, 0),
           (a4, 1, 1, a5)]

    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [F(**dict(zip(p, r))) for r in tab] == [0, 0, 0]:
                print(*p, sep='')