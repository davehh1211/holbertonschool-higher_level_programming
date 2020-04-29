#!/usr/bin/python3
def remove_char_at(str, n):
    for i in str:
        if n < len(str) and n >= 0:
            aux = str.replace(str[n], "")
            return aux
        else:
            return str
