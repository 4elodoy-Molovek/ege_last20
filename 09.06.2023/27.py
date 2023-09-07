f = open('files\\27-1003b.txt')
N = int(f.readline())
K = int(f.readline())
T = int(f.readline())
arr = [int(e) for e in f.read().split()]
mx = 0

sl = []
S = sum(arr[:K])

#        nach  kon  sum
sl.append([0, K - 1, S])
for i in range(K, len(arr)):
    S += arr[i]
    S -= arr[i - K]
    sl.append([i - K + 1, i, S])
sl.sort(key=lambda x: x[2], reverse=True)

for i in range(len(sl) - 1):
    for j in range(i+1, len(sl)):
        if abs(sl[j][0] - sl[i][0]) >= K + T:
            if sl[j][2] + sl[i][2] > mx:
                mx = sl[j][2] + sl[i][2]
                print(mx)
            break
########################################################
# for i in range(0, len(arr) - T - K):
#     b1 = i + K + T
#     b2 = len(arr) - T - 2*K
#     for j in range(i + K + T, len(arr)):
#         arr1 = arr[i:i + K]
#         arr2 = arr[j:j + K]
#         s1 = sum(arr1)
#         s2 = sum(arr2)
#         sc = s1 + s2
#         if sc > mx:
#             mx = sc
# print(mx)
