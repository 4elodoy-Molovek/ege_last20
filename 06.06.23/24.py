def sumchis(x):
    st = str(x)
    summ = 0
    for e in st:
        summ += int(e)
    return summ


f = open('files\\24-232.txt')
s = f.readline()
arr = s.split('0')
arr2 = []
for e in arr:
    if e != '':
        ie = int(e)
        if sumchis(ie) % 5 == 0:
            arr2.append(e)
print(sumchis((int(max(arr2, key=len)))))
