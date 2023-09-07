pzdc = 23*60
f = open('files\\primer.txt')
n = int(f.readline())
k = int(f.readline())
arr = []
for e in f.readlines():
    prib, otb = map(int, e.split())
    arr.append([prib, otb])

stoli = [7*60]*k

