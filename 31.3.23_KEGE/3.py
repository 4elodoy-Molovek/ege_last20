def F(N):
    Nb = bin(N)[2:]
    if Nb.count('1') % 2 == 0:
        Nb = '1' + Nb[:-2] + '01'
    else:
        Nb = '1' + Nb[2:] + '10'

    return int(Nb, 2)


mx = 0
for i in range(1, 10000):
    t = F(i)
    if t <= 100:
        mx = max(mx, t)

print(mx)