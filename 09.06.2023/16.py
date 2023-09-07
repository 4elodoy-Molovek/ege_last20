from sys import setrecursionlimit as srl
from decimal import Decimal

srl(10000)


def F(n):
    if n == 1:
        return Decimal(2)
    else:
        return F(n - 1) * Decimal(Decimal(3 ** n % 5) / Decimal(3 ** n % 7))


print(F(1025) / F(1030))
