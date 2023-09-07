from fnmatch import fnmatch as fn
for i in range(2023, 10**8, 2023):
    if fn(str(i), '671??1*'):
        if i % 2023 == 0:
            print(i, i // 2023)