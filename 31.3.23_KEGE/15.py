def log(x, y, A):
    F = (not((x + 5 < A) <= (y > A))) or (x * y >= 76)
    return F


for A in range(1, 110):
    if all(log(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break
