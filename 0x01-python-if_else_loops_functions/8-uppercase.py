#!/usr/bin/python3
def uppercase(str):
    for let in str:
        if ord(let) >= 97 and ord(let) <= 122:
            let = chr(ord(let) - 32)
        else:
            let = chr(ord(let))
        print("{}".format(let), end='')
    print("")
