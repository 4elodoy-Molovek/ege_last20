f = open('files\\primer.txt')
n, d, t = map(int, f.readline().split())
arr = [int(e) for e in f.readlines()]

mx1 = 0
mx2 = 0
cnt = 0
for i in range(n):
    if arr[i] % d == 0:
        cnt += 1
    if arr[i] % d != 0:
        if mx1 < arr[i]:
            mx1 = arr[i]
        elif mx2 < arr[i] and cnt == t:
            mx2 = arr[i]

print(mx1 + mx2)
