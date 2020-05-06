#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return
    new_list = my_list.copy()
    for i in range(0, len(my_list)):
        if my_list[i] % 2 > 0:
            new_list[i] = False
        else:
            new_list[i] = True
    return new_list
