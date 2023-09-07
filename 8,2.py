from itertools import product as prod
alf = 'ГЕЭ023'
arr = [''.join(e) for e in prod(alf, repeat=7)]
inde = arr.index('ЕГЭ2023') + 1
ind2 = arr.index('2023ЕГЭ') + 1
print(ind2 - inde - 1)
