f = open('files\\24-1005.txt')
s = f.readline()

s = s.replace('A', '1')
s = s.replace('B', '1')
s = s.replace('C', '1')

for e in set(s):
    if e != '1':
        s = s.replace(e, ' ')

arr = s.split()

mx = max(arr, key=len)
print(arr)
print(mx)