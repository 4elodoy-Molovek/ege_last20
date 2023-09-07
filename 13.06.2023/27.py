f = open('files\\27-2005b.txt')
k = int(f.readline())
n = int(f.readline())
Pokaz = []
vrem = 0
for izm in f.readlines():
    vrem += 1
    Pokaz.append([int(izm), vrem])
Pokaz_po_Vel = sorted(Pokaz, reverse=True)
#Pokaz_po_Vrem = Pokaz
Izm1 = max(Pokaz_po_Vel)
SIzm = 0
for i in range(1, n):
    Izm2 = Pokaz_po_Vel[i]
    if abs(Izm1[1] - Izm2[1]) < k:
        continue
    if Pokaz_po_Vel[i - 1][0] < Izm2[0]:
        continue
    if SIzm < (Izm1[0] + Izm2[0]):
        SIzm = Izm1[0] + Izm2[0]
        print(SIzm, Izm1, Izm2)