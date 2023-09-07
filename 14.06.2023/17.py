f = open('files\\17-2003.txt')

arr = [int(e) for e in f.read().split()]
Min_Elem = min(arr)
Max_Sum = 0
Kol = 0
for i in range(1, len(arr)):
    t1, t2 = arr[i - 1], arr[i]
    if (t1 % 117 == Min_Elem) or (t2 % 117 == Min_Elem):
        Kol += 1
        Max_Sum = max(Max_Sum, (t1 + t2))

print(Kol, Max_Sum)
