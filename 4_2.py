my_string = input('Введите текст')
my_dict = {key: my_string.count(key) for key in my_string}
print(my_dict)
'or'
new_dict = {}
for i in my_string:
    new_dict.update({i: my_string.count(i)})
print(new_dict)
