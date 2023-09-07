def to5(n):
    s = ''
    while n > 0:
        s = str(n % 5) + s
        n //= 5

    return s


x = 4 * 625 ** 1920 + 4 * 125 ** 1930 - 4 * 25 ** 1940 - 3 * 5 ** 1950 - 1960
x5 = to5(x)
print(x5.count('0'), x5)
