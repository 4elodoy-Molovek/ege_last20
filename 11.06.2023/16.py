from sys import setrecursionlimit

setrecursionlimit(10000)

arr = [0]*2030
for i in range(2029, 1, -1):
    if i >= 2025:
        arr[i] = i
    else:
        arr[i] = (arr[i + 1] - arr[i+2] + 7)
print(arr[15] - arr[24])

