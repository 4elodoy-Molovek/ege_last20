def F(n, m):
    if n <= 11 and m % 2 == 0:
        return 2 * n
    elif n <= 11 and m % 2 != 0:
        return m
    elif n > 11 and n % 3 == 0:
        return F(n - 1, m + 1) - n + 3
    elif n > 11 and n % 3 != 0:
        return F(n - 2, m + 2) + n
    else:
        return 0


kol = 0
# arr = []
for nn in range(1, 1001):
    t = F(nn, 0)
    if '8' in str(t):
        # arr.append([nn, t])
        kol += 1
# for e in arr:
#     print(e)
# print(len(arr))
print(kol)
