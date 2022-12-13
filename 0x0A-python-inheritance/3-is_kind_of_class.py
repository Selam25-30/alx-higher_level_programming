#!/usr/bin/python3
"""
Module 3-is_kind_of_class

Contain function is_kind_of_class
Return True if the object is an instance of inherited class
"""


def is_kind_of_class(obj, a_class):
    """return True or False by comparing the object with the class
    Notes:
        use type() to get specific class
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of

    Parameters
    ----------
    obj : object
        Instance of the class to compare with a_class
    a_class: class
        A class to compare with obj

    Return
    ---------
    True
        if the object is an instance of inherited class
    False
        otherwise
    """
    return isinstance(obj, a_class)
