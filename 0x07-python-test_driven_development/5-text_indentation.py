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
    marks = [".", ":", "?"]
    for sig in marks:
        text = str(sig + '\n\n').join(char.strip() for char in text.split(sig))
    print(text, end='')

    if len(text) > 0 and text[-1] in marks:
        print('\n')
