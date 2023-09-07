from itertools import product as prod

arr = [''.join(e) for e in prod('АПРЕЛЬ', repeat=5)]
arr.sort(reverse=True)


kol = 0
num = 0
for e in arr:
    num += 1
    if num <= 387:
        if e[-1] == 'Ь':
            kol += 1
print(kol)