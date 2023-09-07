def alg(n):
    nb = bin(n)[2:]
    if n % 3 == 0:
        nb = nb + nb[-3:]
    else:
        nb = nb + bin(3*(n % 3))[2:]
    r = int(nb, 2)
    return r


mx = 0
for i in range(1, 1000):
    if alg(i) < 100:
        mx = max(mx, i)

print(mx)