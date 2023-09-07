def suka(a, b, f1):
    if a == 9:
        f1 = True

    if a == b and f1:
        return 1
    elif a < b:
        return 0
    else:
        return suka(a - 1, b, f1) + suka(a // 2, b, f1)


print(suka(30, 1, False))
