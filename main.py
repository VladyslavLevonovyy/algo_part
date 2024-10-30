def is_in_list(lst, element):
    for el in lst:
        if el == element:
            return True
    return False


def function(list):
    for num in list:

        if not is_in_list(list, -num):
            return num


list_1 = [1, -1, 2, -2, 3]
list_2 = [-3, 1, 2, 3, -1, -4, -2]
list_3 = [1, -1, 2, -2, 3, 3]


print(f"Унікальне число 1: {function(list_1)}")
print(f"Унікальне число 2: {function(list_2)}")
print(f"Унікальне число 3: {function(list_3)}")


my_list = [1, 2, 3]
my_list.pop(2)
print(my_list)

my_list = [1, 2, 3]
del my_list[2]
print(my_list)
