from fnmatch import fnmatch as fn


def IsPalindrome(x):
    s = str(x)
    return s == s[::-1]


qw = []
e8 = []
ans = []

for x in range(1000, 1000000):
    xs = str(x)
    if fn(xs, '33[367]*[67]'):
        qw.append(int(xs))
    elif fn(xs, '8?[149]?*'):
        e8.append(int(xs))

for e in qw:
    for y in e8:
        prz = e * y
        if len(str(prz)) != 9:
            continue
        if IsPalindrome(prz):
            mx = max(e, y)
            ans.append([prz, mx])
ans = sorted(ans)
for e in ans:
    print(e[1], e[0])
