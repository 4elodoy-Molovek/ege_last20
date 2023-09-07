for v1 in '1234567890':
    for v2 in '1234567890':
        s = f'1{v1}34567{v2}9'
        si = int(s)
        if si % 17 == 0:
            print(si, si // 17)