#!/usr/bin/python3
"""
Module 6-base_geometry

Contain parent class BaseGeometry
with public instance method area and integer_validator

Contain subclass Rectangle
with instantation of private attribute width and height, validdate by parent
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    class used to represent Rectangle
    inherits from BaseGeometry

    Parameters
    ---------
    width : positive int, private
        The width of the rectangle
    height : positive int,private
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
