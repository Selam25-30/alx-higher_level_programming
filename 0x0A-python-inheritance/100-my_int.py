#!/usr/bin/python3
"""
Module 100-my_int

Contains class MyInt that inherits from int
Sneaky --> has == and != operators inverted!
"""


class MyInt(int):
    """class MyInt inherit from int

    Parameter
    ---------
    num : interger
        Integer number

    Methods
    --------
    __eq__(self,other)
        compares atttributes of both objects
    __ne__(self, other)
        compares atttributes of both objects
    """
    def __init__(self, num):
        """initalize num attribute

        Parameter
        ---------
        num : interger
            Integer number
        """
        self.num = num

    def __eq__(self, other):
        """compares atttributes of both objects

        Parameter
        ---------
        other : object
            Instance of the class

        Returns:
        ---------
        boolean
            True if both are not equal
            False if both are equal
        """
        return self.num != other

    def __ne__(self, other):
        """compares atttributes of both objects

        Parameter
        ---------
        other : object
            Instance of the class

        Returns:
        ---------
        boolean
            True if both are equal
            False if both are not equal
        """
        return self.num == other
