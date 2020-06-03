#!/usr/bin/python3

"""
function that returns True if the object
is an instance of a class that inherited
(directly or indirectly) from the specified class;
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    issubclass(type(obj),a_class): with this part we check if the object
    is a subclass of that superclass 'a_class' (check inheritage)
    (type(obj) is not a_class): with this part we check that that object
    doesn't belong to that class
    (check that is not that class but a child of that class)
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
