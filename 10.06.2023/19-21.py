from functools import lru_cache as lru


@lru(None)
def game(x, pr):

    steps = [int(a) for a in [x * 1.25, x * 1.5, x * 1.75, x * 2.1] if int(a) <= pr + 215]
    if not steps:
        return 'win'

    if any(game(x, pr) == 'win' for x in steps): return 'p1'
    if all(game(x, pr) == 'p1' for x in steps): return 'v1'
    if any(game(x, pr) == 'v1' for x in steps): return 'p2'
    if all(game(x, pr) in ['p1', 'p2'] for x in steps): return 'v2'


for S in range(4, 173):
    if game(S, S) == 'v2':
        print(S, game(S, S))
