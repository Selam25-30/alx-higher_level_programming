#!/usr/bin/python3
"""
Module 6-base_geometry

Contain class BaseGeometry
with public instance method area and integer_validator
"""


class BaseGeometry:
    """
    A class used to represent Geometry

    Method
    --------
    area(self)
    integer_validator(self, name, value)
    """
    def area(self):
        """
        raises an Exception with the message

        Raises
        --------
        Exception
            when the method is implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Pararmeters
        -----------
        name : str
            Any kind of name
        value : int
            Integer number

        Raises
        ---------
        TypeError
            if value is not integer
        ValueError
            if value is less or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
