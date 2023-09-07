for z41 in range(0, 4):
    for z42 in range(0, 4):
        for z43 in range(0, 4):
            z41, z42, z43 = str(z41), str(z42), str(z43)
            x4 = f'13{z41}{z42}22{z43}'
            for z81 in range(0, 8):
                for z82 in range(0, 8):
                    z81, z82 = str(z81), str(z82)
                    x8 = f'1{z81}{z82}50'
                    for z16 in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']:
                        x16 = f'{z16}C28'
                        if int(x4, 4) == int(x8, 8) == int(x16, 16):
                            print(int(x4, 4))
