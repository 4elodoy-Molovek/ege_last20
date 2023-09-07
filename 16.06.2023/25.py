arr = []
for v1 in '0123456789':
    for v2 in '0123456789':
        for z1 in ' 0123456789':
            s = f'12{v1}{v2}15{z1}6'
            s = s.replace(' ', '')
            x = int(s)
            if x % 253 == 0:
                arr.append(x)
arr.sort()
for e in arr:
    print(e, e//253)