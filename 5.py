def alg(N):
    chet = '02468ACE'
    Nx = hex(N)[2:]
    Nx = Nx.replace('A', '1')
    ChetCount = Nx.count('0') + Nx.count('2') + Nx.count('4') + Nx.count('6') + Nx.count('8') + Nx.count('A') + Nx.count('C') + Nx.count('E')
    if ChetCount > 2:
        Nx = Nx + 'B'
    else:
        Nx = Nx + 'F'
    R = int(Nx, 16)
    return R

for x in range(150, 10000):
    if alg(x) > 3500:
        print(x)
        break