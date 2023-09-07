from functools import lru_cache as lru
from sys import setrecursionlimit as srl

srl(10000)
@lru(None)
def F(n):
    if n < 3:
        return 1
    elif n > 2 and n % 2 != 0:
        return F(n - 1) + n
    else:
        return F(n - 3) + 2 * n


print(F(2048) - F(2041))
