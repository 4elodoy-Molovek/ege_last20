from itertools import product
from itertools import permutations


def F(x, y, z, w):
    return not (x and (y or z) and (z or w) and (y or (not w)))


tab = [(1, 0, 1, 1),
       (1, 1, 0, 0),
       (1, 1, 1, 0),
       (1, 1, 1, 1)]

if len(tab) == len(set(tab)):
    for p in permutations('xyzw'):
        if [F(**dict(zip(p, r))) for r in tab] == [0, 0, 0, 0]:
            print(*p, sep='')