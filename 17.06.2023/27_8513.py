f = open('files\\27_B_8513.txt')
k = int(f.readline())
n = int(f.readline())
arr = [int(e) for e in f.read().split()]

ans = 0  # макс сумма
j = 0  # индекс 2го макс элемента
for i in range(n - k):
    if j - i < k:
        mx = 0  # 2ой макс элемент
        for a in range(i + k, n):
            if arr[a] > mx:
                mx = arr[a]
                j = a
    if arr[i] + arr[j] > ans:
        ans = arr[i] + arr[j]
print(ans)
# Если видим, что мы скшком близко к 2му макс эл-ту, то ищем его заново
