from fnmatch import fnmatch as fn

for i in range(253, 10**8, 253):
    if fn(str(i), '12??15*6'):
        if i % 253 == 0:
            print(i, i//253)