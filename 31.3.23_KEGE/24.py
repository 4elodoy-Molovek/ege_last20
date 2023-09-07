f = open('files\\24_5381.txt')
s = f.readline()

glas = "AEU"
for e in glas:
    s = s.replace(e, 'G')

sogl = "BCDF"
for e in sogl:
    s = s.replace(e, 'S')

s = s.replace('SGSGS', 'SGSSGS')
s = s.replace('SGS', '0')
arr = s.split('0')

ml = 0
for i in range(0, len(arr) - 2):
    t1, t2, t3 = arr[i], arr[i + 1], arr[i + 2]
    tl = len(t1 + t2 + t3) + 4 + 6
    ml = max(tl, ml)
print(ml)

