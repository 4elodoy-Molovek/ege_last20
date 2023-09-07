from functools import lru_cache as lru

@lru(None)
def Velikiy_Izmenitel(a, b, f1, f2, f3):
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
    elif a % 2 == 0:
        return Velikiy_Izmenitel(a - 5, b, f1, f2, f3) + Velikiy_Izmenitel(a - 4, b, f1, f2, f3) + Velikiy_Izmenitel(
            a // 2, b, f1, f2, f3)
    else:
        return Velikiy_Izmenitel(a - 5, b, f1, f2, f3) + Velikiy_Izmenitel(a - 4, b, f1, f2, f3)


print(Velikiy_Izmenitel(100, 2, False, False, False))
