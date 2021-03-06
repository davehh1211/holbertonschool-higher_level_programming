#!/usr/bin/python3
"""Write a function that reads n
lines of a text file (UTF8) and prints it to stdout:
"""


def read_lines(filename="", nb_lines=0):
    """Write a function that reads n
    lines of a text file (UTF8) and prints it to stdout:

    Keyword Arguments:
        filename {str} -- [description] (default: {""})
        nb_lines {int} -- [description] (default: {0})
    """
    count = 0
    with open(filename, encoding='UTF8') as myfile:
        if nb_lines > 0:
            for i in range(nb_lines):
                print(myfile.readline(), end='')
        else:
            print(myfile.read(), end='')
