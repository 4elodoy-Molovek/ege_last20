def lax(s):
    while ('21' in s) or ('31' in s) or ('32' in s):
        s = s.replace('21', '12', 1)
        s = s.replace('31', '13', 1)
        s = s.replace('32', '23', 1)

    return s


for i in range(17, 1000, 3):
    ss = '3'*i + '2'*i + '1'*i
    print(i, lax(ss)[49])
