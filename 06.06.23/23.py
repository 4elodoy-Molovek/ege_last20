from sys import setrecursionlimit as setreclim

setreclim(10000)


def GC(a, b, c2):
    if a == b and c2 < 4:
        return 1
    elif c2 >= 4 or a - b >= 4:
        return 0
    else:
        return GC(a + 3, b, c2) + GC(a - 1, b, c2 + 1)


print(GC(2, 325, 0))
