def log(x, y, A):
    return (x >= 9) or (2 * x < y) or (x * y < A)


for A in range(0, 200):
    if all(log(x, y, A) for x in range(0, 100) for y in range(0, 100)):
        print(A)
