def isp(a, b, f1):
    if a == 30:
        f1 = True
    if a == b and f1:
        return 1
    elif a < b:
        return 0
    else:
        return isp(a - 1, b, f1) + isp(a // 2, b, f1)


print(isp(89, 7, False))
