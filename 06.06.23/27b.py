f = open('files\\27-1001b.txt')
n, m = map(int, f.readline().split())
Doma = [-1]*(m+1)
for e in f.readlines():
    num, kolsem = map(int, e.split())
    Doma[num] = kolsem
MinRast = 999999999999999999999999999999999999
SumRast = 0
RightFams = 0
LeftFams = 0
ans = 0
for i in range(1, m):
    if Doma[i] != -1:
        RightFams += Doma[i]
        SumRast += Doma[i]*i
for i in range(1, m):
    SumRast = SumRast - RightFams + LeftFams
    if Doma[i] != -1:
        RightFams -= Doma[i]
        LeftFams += Doma[i]
    if MinRast >= SumRast and Doma[i] == -1:
        MinRast = SumRast
        ans = i
print(ans)
