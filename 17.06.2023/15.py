def DEL(n, m):
    return n % m == 0


def log(x, A):
    B = range(70, 81)
    return DEL(x, A) or ((x in B) <= (not DEL(x, 18)))


for A in range(1, 100):
    if all(log(x, A) for x in range(1, 100)):
        print(A)
