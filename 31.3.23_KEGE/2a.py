from itertools import *


def f(x, y, z, w):
    F = not (w == y) and (z <= w) and not x
    return F


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    t = [(a1, a2, a3, 1), (1, a4, 1, a5), (0, a6, 1, 0)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                print(*p, sep='')
