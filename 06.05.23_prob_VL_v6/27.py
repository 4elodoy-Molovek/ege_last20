f = open('files\\27-1003test.txt')
n = int(f.readline())
k = int(f.readline())
t = int(f.readline())
arr = [int(e) for e in f.readlines()]
mx = 0

slices = []
S = sum(arr[:k])
#             nach kon sum
slices.append([0, k - 1, S])
for i in range(k, len(arr)):
    S += arr[i]
    S -= arr[i - k]
    slices.append([i - k + 1, i, S])
slices.sort(key=lambda x: x[2], reverse=True)

for i in range(len(slices)-1):
    for j in range(i+1, len(slices)):
        if abs(slices[j][0] - slices[i][1]) >= t:
            if slices[i][2]+slices[j][2] > mx:
                mx = slices[i][2]+slices[j][2]
                print(mx, f'({i}|{j})')
            break


# for i in range(0, n-k-t):
#     for j in range(i+k+t, n-k):
#         b1 = arr[i:i+k]
#         b2 = arr[j:j+k]
#         s1 = sum(arr[i:i+k])
#         s2 = sum(arr[j:j+k])
#         s = s1 + s2
#         mx = max(s, mx)
# print(mx)
