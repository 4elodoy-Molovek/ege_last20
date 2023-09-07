def f(a, b, step):
    if a == b:
        return 1
    if a > b or step > 6:
        return 0
    if a < b:
        return f(a + 1, b, step + 1) + f(a + 2, b, step + 1) + f(a * 2, b, step + 1)


k = 0
A = 1
step = 0
for B in range(34, 60):
    if f(A, B, step):
        k += 1
print(k) #ans = 11
