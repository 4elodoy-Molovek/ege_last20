f = open('files\\27_A_8513.txt')
k = int(f.readline())
n = int(f.readline())
arr = [int(e) for e in f.readlines()]

ind = 0
mxk = 0
mx = 0

for i in range(0, n - k):
    if ind - i <= k:
        mxk = max(arr[i+k:n])
        ind = arr.index(mxk, i+k)
    if arr[i] + mxk > mx:
        mx = mxk + arr[i]
print(mx)