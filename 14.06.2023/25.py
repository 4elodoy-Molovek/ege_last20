def Is_Simple(x):
    for i in range(2, int(x ** 0.5)):
        if x % i == 0:
            return False
    return True


def Prost_Del(x):
    arr = []
    for i in range(2, int(x ** 0.5)):
        if x % i == 0:
            if Is_Simple(i):
                arr.append(i)
            if Is_Simple(x // i):
                arr.append(x // i)
    return arr


for o in range(250_001, 1_000_000):
    S = sum(Prost_Del(o))
    if S != 0 and S % 17 == 0:
        print(o, S)
