def red(s):
    while '12' in s or '22' in s:
        s = s.replace('12', '321', 1)
        s = s.replace('22', '2', 1)
        s = s.replace('32', '3', 1)
        s = s.replace('11', '3', 1)
    return s


def SumCif(s):
    s = str(s)
    sm = 0
    for e in s:
        sm += int(e)
    return sm


for n in range(1, 10000):
    ss = '1' + '2' * n + '1'
    if SumCif((red(ss))) > 3000:
        print(n)
