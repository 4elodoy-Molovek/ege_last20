def sumc(x):
    sumc = 0
    while x > 0:
        sumc = sumc + x % 10
        x = x // 10
    return sumc


def prc(x):
    sumc = 1
    while x > 0:
        i = x % 10
        sumc = sumc * i
        x = x // 10
    return sumc


# print(prc(33), sumc(33))
for x in range(87921, 88188):
    # print(x, sumc(x), prc(x))
    if sumc(x) % 14 == 0 and prc(x) != 0 and prc(x) % 18 == 0:
        print(x, sumc(x), prc(x))
