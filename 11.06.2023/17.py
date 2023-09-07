f = open('files\\17-2006.txt')
arr = [int(e) for e in f.read().split()]

Sim_Pairs = []

for i in range(0, len(arr)//2):
    c1 = arr[i]
    c2 = arr[0 - (i+1)]
    Sim_Pairs.append((c1, c2))

min3 = 99999999999999999999
for e in arr:
    se = str(e)
    if len(se) == 3:
        if (se.count('1') <= 1) and (se.count('2') <= 1) and (se.count('3') <= 1) and (se.count('4') <= 1) and (se.count('5') <= 1) and (se.count('6') <= 1) and (se.count('7') <= 1) and (se.count('8') <= 1) and (se.count('9') <= 1) and (se.count('0') <= 1):
            min3 = min(e, min3)

kol = 0
Min_Sum = 99999999999999999999999999
for pair in Sim_Pairs:
    s1, s2 = pair[0], pair[1]
    if (s1 * s2) % min3 == 0:
        kol += 1
        Min_Sum = min(Min_Sum, (s1 + s2))

print(kol, Min_Sum, min3)
