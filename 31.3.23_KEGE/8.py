from itertools import product as prod

glas = 'AE'
sogl = 'BCD'
arr = [''.join(e) for e in prod("ABCDE", repeat=4)]

n_arr = []
for e in arr:
    if e[-1] in sogl:
        if e[1] in 'ABC' and e[1] != e[0]:
            if e[2] in sogl and e[0] in glas:
                n_arr.append(e)
            elif e[2] in glas and e[0] in sogl:
                n_arr.append(e)
print(len(n_arr))