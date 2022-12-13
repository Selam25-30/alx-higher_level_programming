#!/usr/bin/python3
"""
Module 6-base_geometry

Contain class BaseGeometry
with public instance method area and integer_validator

Contains subclass Rectangle
with instantiation of private attributes width and height, validated by parent,
extends parent's area method and prints with __str__
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class used to represent Rectangle
    inherits from BaseGeometry

    Parameters
    ---------
    width : positive int, private
        The width of the rectangle
    height : positive int, private
        The height of the rectangle
    """
    def __init__(self, width, height):
        """validate and initalize width and height

        Parameters
        ---------
        width : positive int, private
            The width of the rectangle
        height : positive int,private
            The height of the rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """extends parent's empty method and returns area"""
        return self.__width * self.__height

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
