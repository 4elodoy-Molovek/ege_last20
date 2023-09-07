def lol(a, b, f1, f2, f3):
    if a == 73:
        f1 = True
    if a == 22:
        f2 = True
    if a == 50:
        f3 = True

    if a == b and f1 and f2 and not f3:
        return 1
    elif a < b:
        return 0
    else:
        if a % 2 == 0:
            return lol(a - 5, b, f1, f2, f3) + lol(a - 4, b, f1, f2, f3) + lol(a // 2, b, f1, f2, f3)
        else:
            return lol(a - 5, b, f1, f2, f3) + lol(a - 4, b, f1, f2, f3)


print(lol(100, 2, False, False, False))
