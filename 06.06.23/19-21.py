from functools import lru_cache as lru
from sys import setrecursionlimit as srl

srl(10000)


@lru(None)
def game(x):
    if x >= 2200:
        return 'win'

    steps = (x + 2), (x + 3), (x * 2)

    if any(game(x) == 'win' for x in steps): return 'p1'
    if all(game(x) == 'p1' for x in steps): return 'v1'
    if any(game(x) == 'v1' for x in steps): return 'p2'
    if all(game(x) in ['p1', 'p2'] for x in steps): return 'v2'


for s in range(500, 2200):
    # print(s, game(s))
    if game(s) == 'v2':
        print(s)

# 19 2197
# 20 549 1097
# 21 1093
