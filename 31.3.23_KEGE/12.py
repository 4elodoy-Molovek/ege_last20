def red(s):
    while '01' in s:
        if '1' in s:
            s = s.replace('1', '10', 1)
        if '01' in s:
            s = s.replace('01', '1000', 1)
    return s


for n in range(1, 10000):
    ss = '0' * n + '1'
    t = red(ss)
    if t.count('0') > 99:
        print(n)
        break

sss = 25*'0'+'1'
ttt = red(sss)
print(ttt, ttt.count('0'))