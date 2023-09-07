def pepe(n):
    nb = bin(n)[2:]
    n3 = n % 3
    if n3 == 0:
        nb = '10' + nb[2:] + '1'
    elif n3 == 1:
        n3 += nb.count('1')
        nb = bin(n3)[2:] + nb
    elif n3 == 2:
        nb = '11' + '0'*len(nb)
    r = int(nb, 2)
    return r

minr = 999999999999999999999999
for i in range(1, 1000):
    t = pepe(i)
    if t > 1000:
        minr = min(t, minr)
print(minr)