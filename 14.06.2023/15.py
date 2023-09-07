def log(x, A):
    return ((x & 20 != 0) or (x & 55 != 0)) <= ((x & 7 == 0) <= (x & A != 0))


for A in range(1, 1000):
    if all(log(x, A) for x in range(1, 1000)):
        print(A)
        break
