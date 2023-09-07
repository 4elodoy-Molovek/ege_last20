f = open('files\\24.txt')
s = f.readline()
glas = 'AU' # 0
sogl = 'CDF' # 1
s = s.replace('A','0')
s = s.replace('U','0')
s = s.replace('C','1')
s = s.replace('D','1')
s = s.replace('F','1')

kol = 0
mx = 0
for i in range(1, len(s), 2):
    if s[i - 1] == '1' and s[i] == '0':
        kol += 1
        mx = max(mx, kol)
    else:
        kol = 0

print(mx)