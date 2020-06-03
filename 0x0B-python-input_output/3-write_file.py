#!/usr/bin/python3
"""Write a function that
writes a string to a text file
(UTF8) and returns the number of characters written:
"""


def write_file(filename="", text=""):
	"""Write a function that
    writes a string to a text file

	Keyword Arguments:
		filename {str} -- [description] (default: {""})
		text {str} -- [description] (default: {""})

	Returns:
		[int] -- the number of characters written
	"""
    with open(filename, mode='w', encoding='UTF8') as myfile:
        return myfile.write(text)
