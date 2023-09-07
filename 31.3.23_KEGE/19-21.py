from functools import lru_cache as lru
from sys import setrecursionlimit as srl

srl(10000)


@lru(None)
def game(x, y):
    if x + y >= 212:
        return 'win'

    steps = (x + y, y), (x, x + y)

    if any(game(x, y) == 'win' for x, y in steps): return 'p1'
    if all(game(x, y) == 'p1' for x, y in steps): return 'v1'
    if any(game(x, y) == 'v1' for x, y in steps): return 'p2'
    if all(game(x, y) in ['p1', 'p2'] for x, y in steps): return 'v2'


for s in range(1, 112):
    if game(10, s) == 'v2':
        print(s)
