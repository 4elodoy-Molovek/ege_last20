def alg(N):
    for i in range(0, 5):
        if N % 5 == 0:
            N //= 2
        else:
            N -= 1

        if N % 2 != 0:
            N -= 3
        else:
            N -= 2

        if N % 3 != 0:
            N -= 1
        else:
            N //= 3
    return N

mxr = 0
mxn = 0

for n in range(0, 10000):
    tr = alg(n)
    if mxr <= tr:
        mxr = tr
        mxn = n
print(mxn)
print(alg(50))

