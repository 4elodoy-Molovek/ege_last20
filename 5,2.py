def de(N):
    Nb = bin(N)[2:]
    N3 = N % 3
    if N3 == 0:
        Nb = '10' + Nb[2:] + '1'
    elif N3 == 1:
        t = N3 + Nb.count('1')
        t2 = bin(t)[2:]
        Nb = t2 + Nb
    elif N3 == 2:
        Nb = '11' + '0' * len(Nb)
    R = int(Nb, 2)
    return R


ans = 9999999999999999999999999999999
for i in range(1, 10000):
    tt = de(i)
    if tt > 1000:
        ans = min(ans, tt)
print(ans)
