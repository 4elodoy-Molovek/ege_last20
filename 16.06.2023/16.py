def F(n):
    if n < 3:
        return 2
    elif n % 2 == 0:
        return 2 * F(n - 2) - F(n - 1) + 2
    else:
        return 2 * F(n - 1) - F(n - 2) - 2


print(F(17))
