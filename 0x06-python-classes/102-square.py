#!/usr/bin/python3
"""This module contains a class that defines a square.

In the Square class we initialize each object by the
__init__ method with a private instance variable called
__size that takes the size variable's value passed as
argument. Also checks if the size arg has a valid value.
area method returns the area of the square.
"""


class Square:
    """Class that defines a square

    Attributes:
        __size (int): size of the square.
    """
    def __init__(self, size=0):
        """__init__ method that initialize the __size attribute

        Args:
            size (int): Size to initialize the square.
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """size method that set size attribute to value

        Args:
            value (int): Size to set size attribute to.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __call__(self):
        """__call__ method return the value of the square's area"""
        return (self.__size ** 2)

    def __lt__(self, other):
        """__lt__ method compare the instance value with other instance"""
        return self.__size < other.__size

    def ___le__(self, other):
        """__le__ method compare the instance value with other instance"""
        return self.__size <= other.__size

    def __eq__(self, other):
        """__eq__ method compare the instance value with other instance"""
        return self.__size == other.__size

    def __ne__(self, other):
        """__ne__ method compare the instance value with other instance"""
        return self.__size != other.__size

    def __gt__(self, other):
        """__gt__ method compare the instance value with other instance"""
        return self.__size > other.__size

    def __ge__(self, other):
        """__ge__ method compare the instance value with other instance"""
        return self.__size >= other.__size
