import itertools

def check(a,b,c):
    nc = '13579'
    return (a in nc) + (b in nc) + (c in nc) != 3


k = 0
for c in itertools.product('0123456789A', repeat = 6):
    if c[0] != '0' and  all(check(c[i-2],c[i-1],c[i]) for i in range(2, 6)):
        k += 1
print(k, c)