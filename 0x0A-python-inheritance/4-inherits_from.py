#!/usr/bin/python3
"""
Module 4-inherits_from

Contain finction inherits_from
Return True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """Determinre if the object is an insy=tance of a class that
    inherited from specific class

    Parameters
    ----------
    obj : object
        Instance of the class to compare with a_class
    a_class: class
        A class to compare with obj

    Return
    ---------
    True
        if the object is an instance of class that inherited from
        specific class
    False
        otherwise
    """
    return isinstance(obj, a_class) and type(obj) != a_class
