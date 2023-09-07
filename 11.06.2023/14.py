def ToSS(x, n):
    s = ''
    while x > 0:
        s = str(x % n) + s
        x //= n
    return s


a = 7 * 5 ** 123 + 6 * 5 ** 111 - 5 * 25 ** 50 + 4 * 125 ** 30 - 3 * 5 ** 10
a5 = ToSS(a, 5)
print(a5.count('4'))
