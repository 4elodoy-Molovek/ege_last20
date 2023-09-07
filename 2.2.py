print('x y z w')
a = 0, 1
for x in a:
    for y in a:
        for z in a:
            for w in a:
                F = ((x <= y) and ((not z) or (not x) and y)) or ((not w) and z)
                if not F:
                    print(x, y, z, w)
