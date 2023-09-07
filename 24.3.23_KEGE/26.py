f = open('files\\26.txt')
n = int(f.readline())
arr = [int(e) for e in f.read().split()]
arr = sorted(arr, reverse=True)
arr_mn = set(arr)

kol = 1
pih_korob = arr[0]
for i in range(n):
    if pih_korob - arr[i] >= 11:
        kol += 1
        pih_korob = arr[i]
print(kol, pih_korob)
