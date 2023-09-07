def log(x, A):
    F = (((x & 56 != 0) <= (x & 18 != 0)) or (x & A != 0)) <= ((x & 18 == 0) and (x & A == 0) and (x & 43 != 0))
    return F

for A in range(10, 51):
    if all(log(x, A) == 0 for x in range(1, 1000)):
        print(A)