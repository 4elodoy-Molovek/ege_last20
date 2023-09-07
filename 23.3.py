from functools import lru_cache as lru


@lru(None)
def Great_Changer(a, b, f1, ok):
    if a == 31:
        f1 = True
    if a == b and f1:
        return 1
    elif a < b - 2:
        return 0
    elif not ok:
        return Great_Changer(a + 2, b, f1, True) + Great_Changer(a - 3, b, f1, False) + Great_Changer(a // 2, b, f1, False)
    else:
        return Great_Changer(a - 3, b, f1, False) + Great_Changer(a // 2, b, f1, False)


print(Great_Changer(62, 10, False, False))
