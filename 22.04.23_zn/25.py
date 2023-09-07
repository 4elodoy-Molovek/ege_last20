from fnmatch import fnmatch as fn

for i in range(0, 10**8, 237):
    if fn(str(i), '81?2*80') and not fn(str(i), '*9*'):
        print(i, i // 237)