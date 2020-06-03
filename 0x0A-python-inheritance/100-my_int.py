#!/usr/bin/python3
"""Write a class MyList that inherits from list
    """


class MyInt(int):
    """print class inheritance

    Arguments:
        list {[list]} -- [class from the system]
    """

    def __eq__(self, int):
        """rebel int when it is true returns false
        """
        return False

    def __ne__(self, int):
        """rebel int when it is false returns true
        """
        return True
