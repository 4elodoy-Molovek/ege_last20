from functools import lru_cache as lru

@lru(None)
def game(x, y, last):

    if x+y < 162:
        return 'win'

    m = []
    if last != 1 and x > 2:
        m.append((x - 2, y, 1))
    if last != 2 and x > 2:
        m.append((x, y - 2, 2))
    if last != 3 and x > 1:
        m.append((x // 2, y, 3))
    if last != 4 and x > 1:
        m.append((x, y // 2, 4))

    if any(game(x, y, last) == 'win' for x, y, last in m): return 'p1'
    if all(game(x, y, last) == 'p1' for x, y, last in m): return 'v1'
    if any(game(x, y, last) == 'v1' for x, y, last in m): return 'p2'
    if all(game(x, y, last) in ['p1', 'p2'] for x, y, last in m): return 'v2'


for s in range(1, 162):
    if game(17, s, 0) == 'v1':
        print(s)
