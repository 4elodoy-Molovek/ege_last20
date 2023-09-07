def F(n):
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        return F(n // 2) - 1
    elif n > 0 and n % 2 != 0:
        return 2 + F(n - 1)


kol = 0
for i in range(0, 1000):
    if F(i) == 3:
        kol += 1

print(kol)
