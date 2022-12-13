#!/usr/bin/python3
"""
Module 1-my_list

contain class MyList
Inherit from list and has public instance method that print sorted list
"""


class MyList(list):
    """
    Class MyList inherit from List

    Method
    -------
    print_sorted(self)
        print in ascending order
    """
    def print_sorted(self):
        """prints sorted list

        Parameter
        ---------
        obj : object
            a list
        """
        new_list = self[:]
        new_list.sort()
        print(new_list)
