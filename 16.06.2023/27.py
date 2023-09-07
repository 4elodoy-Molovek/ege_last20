from math import ceil

f = open('files\\27-2004b.txt')
n, m = map(int, f.readline().split())
arr = [0]*10000000
for e in f.readlines():
    num, kol_otp = map(int, e.split())
    arr[num] = ceil(kol_otp / m)

SR = 0
SL = 0
Sum = 0
Min_Sum = 999999999999999999999999999999999999999999999999999999999999

for i in range(len(arr)):
    Sum += i * arr[i]
    SR += arr[i]

for i in range(1, len(arr)):
    Sum = Sum - SR + SL
    SR -= arr[i]
    SL += arr[i]
    if arr[i] > 0:
        Min_Sum = min(Sum, Min_Sum)
print(Min_Sum)
