f = open('files\\24.txt')
s = f.readline()
ss = set(s)
for e in ss:
    if e != 'A' and e != 'B' and e != 'C':
        s = s.replace(e, ' ')
arr = s.split()
print(len(max(arr, key=len)) // 2)
