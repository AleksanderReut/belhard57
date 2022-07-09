string1 = input('введите строку')
c=0
for i in string1:
    if string1.count(i) >= 2:
        c+=1
        b=c//2
print(b)