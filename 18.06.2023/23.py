def lax(a, b):
    if a == b:
        return 1
    elif a > b:
        return 0
    else:
        return lax(a + 1, b) + lax(2 * a, b) + lax(2 * a + 1, b)


print(lax(2, 16))
