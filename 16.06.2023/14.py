for x in '0123456789ABCDE':
    s1 = f'99658{x}29'
    s2 = f'102{x}023'
    s = int(s1, 15) + int(s2, 15)
    if s % 14 == 0:
        print(x, s // 14, sep=': ')
