#!/usr/bin/python3
"""This module contains a class that defines a square.

In the Square class we initialize each object by the
__init__ method with a private instance variable called
__size that takes the size variable's value passed as
argument.
"""


class Square:
    """Class that defines a square

    Attributes:
        __size (int): size of the square.
    """
    def __init__(self, size):
        """__init__ method that initialize the __size attribute

        Args:
            size (int): Size to initialize the square.
        """
        self.__size = size
