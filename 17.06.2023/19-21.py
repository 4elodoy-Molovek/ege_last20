from functools import lru_cache as lru


@lru(None)
def game(x):
    if x >= 100:
        return 'win'

    steps = (x + 7), (x * 2)

    if any(game(x) == 'win' for x in steps): return 'p1'
    if any(game(x) == 'p1' for x in steps): return 'v1'
    if any(game(x) == 'v1' for x in steps): return 'p2'
    if all(game(x) in ['p1', 'p2'] for x in steps): return 'v2'


for S in range(1, 100):
    if game(S) == 'v1':
        print(S)
