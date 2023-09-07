f = open('files\\26-2012.txt')
k = int(f.readline())
n = int(f.readline())
Clients = []
Kameri = [0] * k
Last_Used = 0
Kol = 0


for e in f.readlines():
    Prib, Otb = map(int, e.split())
    Clients.append([Prib, Otb + 1])

Clients.sort()

for i in range(n):
    Client = Clients[i]
    for j in range(k):
        if Client[0] >= Kameri[j]:
            Kameri[j] = Client[1]
            Kol += 1
            Last_Used = j + 1
            break

print(Kol, Last_Used)