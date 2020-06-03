#!/usr/bin/python3
"""Write a function that returns the number of lines of a text file:
"""


def number_of_lines(filename=""):
    """Write a function that returns the
    number of lines of a text file:

    Keyword Arguments:
        filename {str} -- [description] (default: {""})

    Returns:
        count -- [int of iterations]
    """
    count = 0
    with open(filename, encoding='UTF8') as myfile:
        for line in myfile:
            count += 1
    return (count)
