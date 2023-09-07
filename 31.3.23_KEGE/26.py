f = open('files\\primer.txt')
N, S = map(int, f.readline().split())
arr = []
for s in f.readlines():
    ts = s.split()
    k = int(ts[0]) + 10
    o = int(ts[1])
    arr.append([k, o])

