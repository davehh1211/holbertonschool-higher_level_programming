#!/usr/bin/python3
"""Write a function
that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """Write a function
    that reads a text file (UTF8)
    and prints it to stdout:

        Keyword Arguments:
                filename {str} -- [description] (default: {""})
        """
    with open(filename, encoding='UTF8') as myfile:
        for line in myfile:
            print(line, end='')
