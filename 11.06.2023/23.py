def pepe(a, b, kol):
    if a == b and kol == 4:
        return 1
    elif a > b or kol > 4:
        return 0
    else:
        return pepe(a + 2, b, kol + 1) + pepe(a * 3, b, kol + 1)


arr = []
for i in range(1, 200):
    if pepe(1, i, 0):
        arr.append(i)
print(len(set(arr)))
