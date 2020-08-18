#!/usr/bin/python3
"""modulo peak
"""


def find_peak(list_of_integers):
	"""Write a function that finds a peak in a list of unsorted integers.

	Args:
		list_of_integers ([type]): [description]

	Returns:
		[type]: [description]
	"""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
