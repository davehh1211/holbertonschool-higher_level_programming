#!/usr/bin/python3
"""Write a function that inserts a line
of text to a file, after each line containing
a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Write a function that inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename (str, optional): [file to open]. Defaults to "".
        search_string (str, optional): [str to compare]. Defaults to "".
        new_string (str, optional): [new str to append]. Defaults to "".
    """
    with open(filename, mode='r', encoding='UTF8') as myfile:
        line_newstr = ""
        for i in myfile:
            if search_string in i:
                line_newstr += i + new_string
            else:
                line_newstr += i
    with open(filename, mode='w', encoding='UTF8') as myfile:
        myfile.write(line_newstr)
