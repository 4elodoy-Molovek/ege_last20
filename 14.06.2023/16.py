def F(n):
    if n > 15:
        return n * n - 5
    else:
        return n * F(n + 2) + n + F(n + 3)


print(F(1))
