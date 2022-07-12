def binary(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s


print(binary(4))


