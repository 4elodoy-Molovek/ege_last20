from fnmatch import fnmatch as fn

for i in range(1, 10 ** 7):
    if fn(str(i), '?4?*'):
        for j in range(1, 10 ** 7):
            if i * j > 10 ** 7:
                break
            else:
                if fn(str(j), '128*'):
                    if (i + j) % 2027 == 0:
                        print(i, j)