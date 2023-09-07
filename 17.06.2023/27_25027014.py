f = open('files\\27A_25027014.txt')
k = int(f.readline())
n = int(f.readline())
arr = [int(e) for e in f.read().split()]


ans = []


for i in range(0, n - k):
    t1 = arr[i]
    t2 = arr[i + k]
    ans.append(t1 + t2)

print(max(ans))
