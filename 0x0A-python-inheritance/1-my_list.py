#!/usr/bin/python3
"""Write a class MyList that inherits from list
    """


class MyList(list):
    """print class inheritance

    Arguments:
        list {[list]} -- [class from the system]
    """

    def print_sorted(self):
        """sorts the list ascendent
        """
        print(sorted(self))
