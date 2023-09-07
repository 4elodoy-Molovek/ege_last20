print('x y z w')
a = 0,1
for x in a:
    for y in a:
        for z in a:
            for w in a:
                F = not(w == y) and (z <= w) and not x
                if F:
                    print(x, y, z, w)
                    