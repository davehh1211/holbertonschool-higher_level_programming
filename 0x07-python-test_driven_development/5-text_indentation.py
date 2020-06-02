#!/usr/bin/python3
""" It splits a string when a character is found.
"""


def text_indentation(text):
    """ function that splits a string when a character appears.

    Arguments:
        text {[string]} -- A text given by the user

    Raises:
        TypeError: text must be a string - when the string is not its type

    Special Characters: characters that parses the string {.} {:} {?}
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    runner = ":"
    for i in text:
        if i is " " and runner in ".?:":
            continue
        print(i, end="")
        if i in ".:?":
            print("\n")
        runner = i
