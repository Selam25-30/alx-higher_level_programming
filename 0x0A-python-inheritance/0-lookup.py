#!/usr/bin/python3
"""
Module 0-lookup

Contain function lookup
Return list of object's attribute and method
"""


def lookup(obj):
    """Returns a list of objects's attribute and method

    Parameter
    ----------
    obj : object
        Instance of a class

    Returns
    ----------
    list
        a list of object's attribute and method
    """
    return dir(obj)
