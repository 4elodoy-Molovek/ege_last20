def alg(n):
    nb = bin(n)[2:]
    if n % 2 == 0:
        nb = '1' + nb + str(nb.count('1') % 2)
    else:
        nb = nb + '0' + str(nb.count('1') % 2)
    r = int(nb, 2)
    return r


mn = 9999999999999999999999999999999999999999999999999999999
ans = 0
for i in range(1, 100):
    t = alg(i)
    if t > 100:
        mn = min(mn, t)
        print(t, i)
