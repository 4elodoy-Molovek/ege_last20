from sys import setrecursionlimit as srl

srl(10000)


arr = [0]*10**6
for i in range(10 ** 5 + 1):
    if i >= 10 ** 5:
        arr[i] = 3
    elif i <= 3689:
        arr[i] = 1
    elif i % 2 == 0:
        arr[i] = arr[i + 2] + arr[i + 4]
    elif i % 2 != 0:
        arr[i] = arr[i - 2] + arr[i - 6]
print(str(arr[7680] - arr[99241]))
