from functools import lru_cache as lru


@lru(None)
def game(x):
    if x >= 55:
        return 'win'

    steps = (x + 1), (x + 4), (x * 3)

    if any(game(x) == 'win' for x in steps): return 'p1'
    if all(game(x) == 'p1' for x in steps): return 'v1'
    if any(game(x) == 'v1' for x in steps): return 'p2'
    if all(game(x) in ['p1', 'p2'] for x in steps): return 'v2'


for S in range(1, 55):
    if game(S) == 'v2':
        print(S)
