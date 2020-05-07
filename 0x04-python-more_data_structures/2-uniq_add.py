#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = set()
    sum = 0
    for i in range(len(my_list)):
        if my_list[i] not in s:
            s.add(my_list[i])
    for i in s:
        sum = sum + i
    
    return sum
