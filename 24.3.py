def NChetCont(x):
    s = str(x)
    chet = '13579'
    for e in chet:
        if e in s:
            return False
    return True


f = open('24-1003.txt')
ss = f.readline()
chet = '02468'
# alf = '0123456789ABCDEF'
alfp = 'qwrtyuiopsghjklzxvnmQWRTYUIOPSGHJKLZXVNM'
for x in alfp:
    ss = ss.replace(x, ' ')
ss = ss.split()

mx = 0
for e in ss:
    ei = int(e, 16)
    if NChetCont(ei):
        mx = max(mx, ei)
print(mx)


