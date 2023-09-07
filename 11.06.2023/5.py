def alg(n):
    nb = bin(n)[2:]
    if n % 5 == 0:
        nb = '1' + nb + nb[-2:]
    else:
        nb = bin(n % 5)[2:] + nb
    r = int(nb, 2)
    return r


for i in range(1, 100):
    if alg(i) <= 223:
        print(alg(i))
