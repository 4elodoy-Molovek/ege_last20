from itertools import product
from itertools import permutations


def F(x, y, z, w):
    return (w == (z <= x)) and y


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    tab = [(a1, 0, a2, 0),
           (1, a3, 1, 1),
           (a4, a5, 0, 0)]

    if len(tab) == len(set(tab)):
        for p in permutations("xyzw"):
            if [F(**dict(zip(p, r))) for r in tab] == [1, 0, 1]:
                print(*p, sep='')
