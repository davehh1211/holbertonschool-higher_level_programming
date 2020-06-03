#!/usr/bin/python3
"""Write a function that returns True
if the object is an instance of, or
if the object is an instance of a class
that inherited from, the specified class;
otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """issubclass(type(obj),a_class): with this part we check if the object
is a subclass of that superclass 'a_class' (check inheritage)
(type(obj) is not a_class): with this part we check that that object
doesn't belong to that class
(check that is not that class but a child of that class)

Arguments:
    obj {[any]} -- [description]
    a_class {[class]} -- [description]

Returns:
    [true or false]
"""
    return isinstance(obj, a_class)
