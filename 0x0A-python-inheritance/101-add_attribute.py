#!/usr/bin/python3
"""
Module 101-add_attribute

Contains function that adds new attribute if possible
"""


def add_attribute(obj, attr, value):
    """
    add attribute to an object if it’s possible
    """
    if "__dict__" in dir(obj):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
