#!/usr/bin/python3
def print_list_integer(my_list=[]):
    list = my_list[:]
    for i in list:
        print("{}".format(list.index(i)))
