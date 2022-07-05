value_name = input('Введите значение ключа name')
value_email = input('Введите значение ключа email')
my_dict = {key: {'name': value_name, 'email': value_email} for key in range(10)}
print(my_dict)
