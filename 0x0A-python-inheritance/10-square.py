#!/usr/bin/python3
"""
Module 10-square

Contain class BaseGeometry
with public instance method area and integer_validator

Contain  subclass Rectangle
with instantiation of private attributes width and height, validated by parent,
extends parent's area method and prints with __str__

Contain subclass Square
with instantation of private attribute size, validate by superclass
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Class tha represent Square
    inherit from Rectangle

    parameter
    ---------
    size : positive int, private
        The side of the square
    """
    def __init__(self, size):
        """validate and initalize size
        parameter
        ---------
        size : positive int, private
            The side of the square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return super().__str__()
