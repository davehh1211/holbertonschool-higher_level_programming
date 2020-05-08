#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or not roman_string:
        return 0
    romandict = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50),
                      ('C', 100), ('D', 500), ('M', 1000)])
    inte = 0
    for cur_num, nex_num in zip(roman_string, roman_string[1:]):
        if romandict[cur_num] < romandict[nex_num]:
            inte -= romandict[cur_num]
        else:
            inte += romandict[cur_num]
    inte += romandict[roman_string[-1]]
    return inte
