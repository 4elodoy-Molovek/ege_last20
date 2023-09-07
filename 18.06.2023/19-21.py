from functools import lru_cache as lru


@lru(None)
def game(x):
    steps = (x + 7), (x * 2)
    if x >= 100:
        return 'win'

    if any(game(x) == 'win' for x in steps): return 'p1'
    if all(game(x) == 'p1' for x in steps): return 'v1'
    if any(game(x) == 'v1' for x in steps): return 'p2'
    if all(game(x) in ['p1', 'p2'] for x in steps): return 'v2'


for S in range(1, 100):
    print(S, game(S))

############# 19 #############
# p1 - 50-99
# v1 - 29-49

############# 20 #############
# &&&&&&&&

############# 21 #############
# 29
