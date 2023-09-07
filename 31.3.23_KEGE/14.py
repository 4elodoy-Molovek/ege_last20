def IsSimple(x):
    for i in range(2, int(x ** 0.5)):
        if x % i == 0:
            return False
    return True


kol = 0
for x in '0123456789abcdefgh':
    s1 = f'56{x}3'
    s2 = f'4{x}9'
    s3 = f'57{x}1'
    ss = int(s1, 18) + int(s2, 18) - int(s3, 18)
    if IsSimple(ss):
        kol += 1
print(kol)