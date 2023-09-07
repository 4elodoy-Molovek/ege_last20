def lol(a, b):
    if a == b:
        return 1
    elif a > b:
        return 0
    else:
        return lol(a + 1, b) + lol(a * 2, b)


print(lol(1, 16))
