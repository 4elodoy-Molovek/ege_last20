from itertools import permutations
from itertools import product


def F(a, b, c, d):
    return a and (not b) or (a or b) and c or d


for a1, a2, a3, a4, a5, a6, a7, a8 in product([0, 1], repeat=8):
    tab = [(a1, a2, a3, 1),
           (a4, 1, a5, 1),
           (1, a6, a7, a8)]
    if len(tab) == len(set(tab)):
        for p in permutations("abcd"):
            if [F(**dict(zip(p, r))) for r in tab] == [0, 0, 0]:
                print(*p, sep='')