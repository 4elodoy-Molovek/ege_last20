print('x y z w t')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                for t in 0, 1:
                    F = ((x and y) or (y and (z <= (not w))) or ((not t) == (not x))) == ((not z) and t)
                    if F:
                        print(x, y, z, w, t)
