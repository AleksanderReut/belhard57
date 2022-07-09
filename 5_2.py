num1 = int(input('введите первое число'))
operation = input('введите операцию')
num2 = int(input('введите второе число'))
if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '**':
    print(num1 ** num2)
elif operation == '/':
    print(num1 / num2)
else:
    print('вы ввели не правельную операцию')
