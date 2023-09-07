from functools import lru_cache as lru


@lru(None)
def game(x, y):
    if x >= 50 or y >= 50:
        return 'win'

    steps = (x + 3, y), (x, y + 3), (x * 2, y), (x, y * 2)

    if any(game(x, y) == 'win' for x, y in steps): return 'p1'
    if all(game(x, y) == 'p1' for x, y in steps): return 'v1'
    if any(game(x, y) == 'v1' for x, y in steps): return 'p2'
    if all(game(x, y) in ['p1', 'p2'] for x, y in steps): return 'v2'


for S in range(1, 28):
    if game(22, S) == 'v2':
        print(S)

