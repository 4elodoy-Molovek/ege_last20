from sys import setrecursionlimit as srl

srl(10000)
def F(n):
    if n > 3456:
        return n + 1
    elif n % 3 == 0:
        return F(n + 1) + F(n + 2)
    else:
        return F(n + (n % 3)) + 2


print(F(12) - F(17))
