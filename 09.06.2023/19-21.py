from functools import lru_cache as lru
from sys import setrecursionlimit as srl

srl(10000)


@lru(None)
def game(x, y, pt):
    if x + y < 162 and x >= 0 and y >= 0:
        return 'win'
    if x < 0 or y < 0:
        return 0

    if pt == 1:
        steps = (x, y - 2, 2), (x // 2, y, 3), (x, y // 2, 4)
    elif pt == 2:
        steps = (x - 2, y, 1), (x // 2, y, 3), (x, y // 2, 4)
    elif pt == 3:
        steps = (x - 2, y, 1), (x, y - 2, 2), (x, y // 2, 4)
    elif pt == 4:
        steps = (x - 2, y, 1), (x, y - 2, 2), (x // 2, y, 3)
    else:
        steps = (x - 2, y, 1), (x, y - 2, 2), (x // 2, y, 3), (x, y // 2, 4)

    if any(game(x, y, pt) == 'win' for x, y, pt in steps): return 'p1'
    if all(game(x, y, pt) == 'p1' for x, y, pt in steps): return 'v1'
    if any(game(x, y, pt) == 'v1' for x, y, pt in steps): return 'p2'
    if all(game(x, y, pt) in ['p1', 'p2'] for x, y, pt in steps): return 'v2'


for s in range(144, 1000):
    if game(17, s, 0) == 'v2':
        print(s, game(17, s, 0))
