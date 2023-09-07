arr = []
for z1 in ' 0123456789':
    for z2 in ' 0123456789':
        s = f'1234{z1}{z2}54'
        s = s.replace(' ', '')
        ch = int(s)
        if ch % 21 == 0:
            arr.append(ch)


arr = set(arr)
arr = sorted(arr)
for e in arr:
    print(e, e//21)
