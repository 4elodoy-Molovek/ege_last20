def log(x, y, z, A):
    F = ((2 * x + y) != 136) or ((z * y) < 100) or ((A ** 2) >= (x + y))
    return F


for A in range(0, 1000):
    if all(log(x, y, z, A) for x in range(0, 100) for y in range(0, 100) for z in range(0, 100)):
        print(A)
        break
