f = open('files\\27-2005b.txt')
k = int(f.readline())
n = int(f.readline())
Pokaz = []
for izm in f.readlines():
    Pokaz.append(int(izm))

Mx1, Mx_Ind1 = 0, 0
Mx2, Mx_Ind2 = 0, 0
SIzm = 0

for i in range(0, n):
    if Pokaz[i] > Mx1:
        if i - Mx_Ind1 >= k and Mx1 + Pokaz[i] > SIzm:
            SIzm = Mx1 + Pokaz[i]
        elif i - Mx_Ind2 >= k and Mx2 + Pokaz[i] > SIzm:
            SIzm = Mx2 + Pokaz[i]

        Mx2 = Mx1
        Mx_Ind2 = Mx_Ind1
        Mx1 = Pokaz[i]
        Mx_Ind1 = i
print(SIzm)
