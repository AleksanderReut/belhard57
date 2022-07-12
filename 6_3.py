def move(s, n):
    return s[n:] + s[:n]


num = int(input('Введите число для смещения'))
list1 = [1, 2, 3, 4, 5, 6, 7]
print(move(list1, num))




