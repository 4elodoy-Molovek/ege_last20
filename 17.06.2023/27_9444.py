f = open('files\\27B_9444.txt')
n = int(f.readline())
arr = [int(e) for e in f.read().split()]

mx1 = 0
mx2 = 0

for i in range(n):
    if arr[i] % 49 != 0 and arr[i] % 7 == 0:
        if arr[i] > mx1:
            mx1 = arr[i]
    elif arr[i] % 7 != 0:
        if arr[i] > mx2:
            mx2 = arr[i]

print(mx1*mx2)
