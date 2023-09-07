from functools import lru_cache as lru


#@lru(None)
def pepe(a, b):
    if a == b:
        return 1
    elif a > b:
        return 0
    else:
        return pepe(a + 1, b) + pepe(a + 5, b) + pepe(a * 3, b)


for i in range(1, 1000):
    if pepe(1, i) == 175:
        print(i)
