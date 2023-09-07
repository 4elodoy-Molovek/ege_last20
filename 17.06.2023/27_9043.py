f = open('files\\27B_9043.txt')
n = int(f.readline())
k = int(f.readline())
arr = [int(e) for e in f.readlines()]

Max_Ind1 = 0
Max_Ind2 = 0
Max_Ind_Raz = 0
Max_Sum = 0
Ind_2 = 0

for i in range(n - k):
    if Ind_2 - i < k:
        Max_2 = 0
        for j in range(i + k, n):
            if arr[j] >= Max_2:
                Max_2 = arr[j]
                Ind_2 = j
    if arr[i] + arr[Ind_2] > Max_Sum:
        Max_Sum = arr[i] + arr[Ind_2]
        Max_Ind2 = Ind_2
        Max_Ind1 = i
        Max_Ind_Raz = 0
        if Max_Ind2 - Max_Ind1 > Max_Ind_Raz:
            Max_Ind_Raz = Max_Ind2 - Max_Ind1

    elif arr[i] + arr[Ind_2] == Max_Sum:
        Max_Sum = arr[i] + arr[Ind_2]
        Max_Ind2 = Ind_2
        Max_Ind1 = i
        if Max_Ind2 - Max_Ind1 > Max_Ind_Raz:
            Max_Ind_Raz = Max_Ind2 - Max_Ind1

print(Max_Ind_Raz)