def Int_to_Arr(x):
    s = str(x)
    arr = []
    for e in s:
        arr.append(int(e))
    return arr


def Proiz_Dig(x):
    proiz = 1
    arr = Int_to_Arr(x)
    for e in arr:
        proiz *= e
    return proiz


Ans_Arr = []
for i in range(87921, 88188):
    PD = Proiz_Dig(i)
    SD = sum(Int_to_Arr(i))
    if (SD % 14 == 0) and (PD % 18 == 0) and (PD != 0):
        Ans_Arr.append([PD, SD])
Ans_Arr.sort()
for e in Ans_Arr:
    print(e[1], e[0], sep=' ')
