#!/usr/bin/python3
"""
Module 2-is_same_class

Contain function is_same_class
Return True if the instance is object of specified class or False
"""


def is_same_class(obj, a_class):
    """return True or False by comparing the object with the class
    Notes:
        use type() to get specific class
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of

    Parameters
    ----------
    obj : object
        Instance of the class to compare with a_class
    a_class : class
        A class to compare with ogj

    Return
    --------
    True
        if the object is exactly an instance of the specified class
    False
        otherwise
    """
    return type(obj) == a_class
