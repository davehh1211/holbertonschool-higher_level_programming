#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        a = 0
        b = 0
        for score, weight in my_list:
            a += score * weight
            b += weight
        return a / b
    return 0
