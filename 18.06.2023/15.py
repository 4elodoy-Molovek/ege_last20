def log(x, A):
    return ((x & 7 != 0) <= ((x & A != 0) <= (x & 54 != 0))) <= ((x & 27 == 0) and (x & A != 0) and (x & 7 != 0))


kol = 0
for A in range(1, 100000):
    if all(log(x, A) == 0 for x in range(1, 100000)):
        kol += 1

print(kol)
