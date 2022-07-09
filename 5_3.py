num = 0

for i in range(2,100):
    if i % 2 == 0:
        print(i, end=' ')
        num+=1
        if num > 4:
            num *= 0
            print('\n')
