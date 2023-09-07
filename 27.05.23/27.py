f = open('files\\27B_8381.txt')
N, D, T = map(int, f.readline().split())
arr = [int(e) for e in f.readlines()]
kol_par = 0
for i in range(0, N - T):
    for j in range(i + T, N):
        kol = 0
        arrw = arr[i:j]
        for e in arrw:
            if e % D == 0:
                kol += 1
        if kol == T and arr[i] % D != 0 and arr[j] % D != 0:
            kol_par += 1
print(kol_par)

#############################################################################

kol_par = 0
neD = [0]
for e in arr:
    if e % D == 0:
        neD.append(0)
    else:
        neD[-1] += 1
for i in range(0, len(neD) - T):
    t1, t2 = neD[i], neD[i + T]
    kol_par += t1 * t2
print(kol_par)
