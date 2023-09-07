from functools import lru_cache as lru
from sys import setrecursionlimit

setrecursionlimit(10000)


@lru(None)
def game(x, y):
    if x + y >= 892:
        return 'win'

    steps = (x + 2, y), (x, y + 2), (x * 2, y), (x, y * 2)

    if any(game(x, y) == 'win' for x, y in steps): return 'p1'
    if all(game(x, y) == 'p1' for x, y in steps): return 'v1'
    if any(game(x, y) == 'v1' for x, y in steps): return 'p2'
    if all(game(x, y) in ['p1', 'p2'] for x, y in steps): return 'v2'


for S in range(1, 855):
    if game(37, S) == 'v2':
        print(S)
