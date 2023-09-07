f = open('files\\27-1002b.txt')
n = int(f.readline())
k = int(f.readline())
arr = [int(e) for e in f.readlines()]
mx, sm = 0, 0

mj1 = max(arr[k:n - k])
mj1i = arr.index(mj1, k)

mj2 = max(arr[mj1i + k:n])
mj2i = arr.index(mj2, mj1i + k)

for i in range(0, n - 2 * k):
    rast1 = mj1i - i
    if rast1 < k:
        mj1 = max(arr[i + k:n - k])
        mj1i = arr.index(mj1, i + k)

        mj2 = max(arr[mj1i + k:n])
        mj2i = arr.index(mj2, mj1i + k)

    sm = max(sm, (mj1 + mj2 + arr[i]))

print(sm)
