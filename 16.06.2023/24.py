from itertools import product
f = open('files\\24-2010.txt')
s = f.readline()
xyz = [''.join(e) for e in product('XYZ', repeat=2)]

arr = []
ts = ''
for i in range(1, len(s)):
    if (s[i - 1] + s[i]) not in xyz:
        ts += s[i - 1]
    else:
        arr.append(ts)
        ts = ''

print(len(max(arr, key=len)) + 1)