def log(x, y, A):
    F = (x >= 27) or (2*x < 3*y) or ((x+2)*(y-3) < A)
    return F



for A in range(1, 1000):
    if all(log(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)