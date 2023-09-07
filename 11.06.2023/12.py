def red(s):
    while '555' in s or '11' in s or '2' in s:
        s = s.replace('555', '1', 1)
        s = s.replace('11', '25', 1)
        s = s.replace('2', '5', 1)
    return s


mxs = 0
mnn = 999999999999999999999999999999999999
for n in range(101, 1000):
    if n % 9 != 0:
        continue
    s = '5' * n
    t = red(s)
    if int(t) > mxs:
        mxs = int(t)
        mnn = n
        print(mxs, mnn)
