#!/usr/bin/python3
"""Write a function that appends a
string at the end of a text file (UTF8)
and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """Write a function that appends a
    string at the end of a text file

    Keyword Arguments:
        filename {str} -- [description] (default: {""})
        text {str} -- [description] (default: {""})

    Returns:
        [int] -- [returns the number of characters added]
    """
    with open(filename, mode='a', encoding='UTF8') as myfile:
        return myfile.write(text)
