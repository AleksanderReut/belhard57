num_1 = int(input('введите первое число'))
num_2 = int(input('введите второе число'))
num_3 = int(input('введите третье число'))
if num_1 > 0 and num_2 > 0 and num_3 > 0:
    print(f'Все числа положительные: {num_1}, {num_2}, {num_3}')
elif num_1 < 0 and num_2 < 0 and num_3 < 0:
    print(f'Все числа отрицательные {num_1}, {num_2}, {num_3}')