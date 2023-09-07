for z1 in ' 0123456789':
    for z2 in ' 0123456789':
        for v1 in '0123456789':
            for v2 in '0123456789':
                s = f'{z1}{z2}1{v1}542{v2}'
                s = s.replace(' ', '')
                si = int(s)
                if si % 2084 == 0:
                    print(si, si//2084)