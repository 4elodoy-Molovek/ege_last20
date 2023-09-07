def dd(x):
    ddc = ''
    ss = str(x)
    for e in ss:
        ts = bin(int(e))[2:]
        ts = '0' * (4 - len(ts)) + ts
        ddc += ts
    return ddc


def alg(n):
    ndd = dd(n)
    nb = ndd.replace('0', 'n')
    nb = nb.replace('1', '0')
    nb = nb.replace('n', '1')
    r = int(nb, 2)
    return r


for N in range(1, 1000):
    if alg(N) == 151:
        print(N)
