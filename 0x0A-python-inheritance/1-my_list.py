#!/usr/bin/python3
"""[summary]
    """


class MyList(list):
	"""[summary]

	Arguments:
		list {[type]} -- [description]
	"""
    def print_sorted(self):
        c = sorted(self)
        print(c)
