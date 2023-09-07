f = open('files\\24-2005.txt')
s = f.readline()
s = s.replace('EA', '2')
s = s.replace('NPC', '3')
for e in set(s):
    if (e != '2') and (e != '3'):
        s = s.replace(e, ' ')
arr = s.split()
Max_Len = 0
for P_Psl in arr:
    T_Len = 0
    for e in P_Psl:
        T_Len += int(e)
    Max_Len = max(Max_Len, T_Len)
print(Max_Len)