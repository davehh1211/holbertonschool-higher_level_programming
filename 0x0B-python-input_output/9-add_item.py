#!/usr/bin/python3
"""Write a script that adds all arguments
to a Python list, and then save them to a file
"""


import sys
import os

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    """main
    """
    filename = "add_item.json"
    if os.path.isfile(filename):
        "evaluate if the filename exist"
        listin = load_from_json_file(filename)
        "loads the list file if it exists"
        listin += sys.argv[1:]
        "it concatenates the list with the new arguemnts"
        save_to_json_file(list(listin), filename)
        "it saves the arguments"
    else:
        "if the file does not exist, it creates it."
        save_to_json_file(sys.argv[1:], filename)
