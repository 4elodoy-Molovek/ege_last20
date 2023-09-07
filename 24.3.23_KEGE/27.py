# 44 anal\cont - max
# Stoimost = rast*Kol_cont
# ob_stoimost = sum(stoimost)
# min(ob_stoimost - ?)
from math import ceil

f = open('files/27_B.txt')

n = int(f.readline())
arr = []
for i in f.readlines():
    num, kol_prob = map(int, i.split())
    kol_cont = ceil(kol_prob / 44)
    arr.append([num, kol_prob, kol_cont])
st_arr = []

for i in range(n):
    stoim = 0
    for j in range(n):
        rast = abs(arr[i][0] - arr[j][0])
        stoim += (rast*arr[j][2])
    st_arr.append(stoim)
print(min(st_arr))



