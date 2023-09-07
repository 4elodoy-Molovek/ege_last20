def alg(s):
    while '25' in s or '355' in s or '555' in s:
        s = s.replace('25', '5', 1)
        s = s.replace('355', '52', 1)
        s = s.replace('555', '3', 1)
    return s


for n in range(4, 1000):
    s = '2' + '5' * n
    if alg(s).count('3') == 2:
        print(n)
        break