def PoVozr(x):
    x = str(x)
    xs = ''.join(sorted(x))
    if x == xs:
        return True
    return False


f = open('files\\24-4.txt')
s = f.readline()
for e in set(s):
    if e not in '0123456789':
        s = s.replace(e, ' ')
arr = s.split()

arrw = []
for posl in arr:
    if PoVozr(posl):
        arrw.append(posl)
print(max(arrw, key=len))

