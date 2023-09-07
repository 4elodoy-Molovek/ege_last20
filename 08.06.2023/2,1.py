from itertools import product
from itertools import permutations


def f(x, y, z, w, t):
    return ((x and y) or (y and (z <= (not w))) or ((not t) == (not x))) == ((not z) and t)


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    tab = [(1, 1, 0, 1, 1),
         (0, 1, 0, 0, 1),
         (0, 1, 1, 0, 0),
         (0, 1, 1, 1, 1),
         (1, 0, 0, 0, 0)]
    if len(tab) == len(set(tab)):
        for p in permutations("xyzwt"):
            if [f(**dict(zip(p, r))) for r in tab] == [1, 1, 1, 1, 1]:
                print(*p, sep='')
