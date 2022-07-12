def sort_str(start_list):
    for i in start_list:
        if type(i) == str:
            print(i)


list1 = [1, 2, 3, 4, 5,'21321', [2, 3, 4, 5], 'cat']
sort_str(list1)
