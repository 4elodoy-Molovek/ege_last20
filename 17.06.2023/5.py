def alg(n):
    nb = bin(n)[2:]
    if n % 2 != 0:
        nb = '1' + nb + '11'
    else:
        nb = '11' + nb + '00'
    r = int(nb, 2)
    return r


for i in range(1000):
    rr = alg(i)
    if rr < 127:
        print(rr, i)
