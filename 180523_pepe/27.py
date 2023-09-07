f = open('files\\27_A.txt')
k = int(f.readline())
n = int(f.readline())
arr = [int(e) for e in f.readlines()]

ind = 0
mxk = 0
mx = 0
chet = []
nechet = []

for i in range(len(arr)):
    if arr[i] % 2 == 0 and arr[i] % 26 == 0:
        chet.append([arr[i], i])
    elif arr[i] % 2 != 0:
        nechet.append([arr[i], i])

chet.sort(reverse=True)
nechet.sort(reverse=True)
for i in chet:
    for j in nechet:
        if i[0] + j[0] < mx:
            break
        if abs(i[1] - j[1]) >= k:
            mx = max(mx, (i[0] + j[0]))
print(mx)
