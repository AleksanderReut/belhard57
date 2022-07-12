def reverse_list(start_list):
    new_list = []
    for i in range(len(start_list)-1, -1, -1):
        new_list.append(start_list[i])
    return new_list


list1 = [1, 2, 3, 4, 5, 6]
print(reverse_list(list1))
