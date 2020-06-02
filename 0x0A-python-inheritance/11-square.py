#!/usr/bin/python3
"""This module contain classes called BaseGeometry, Rectangle, Square"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """area method
        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator method that validate integer

        Args:
            name (str): is a string
            value (int): is a integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class

    Args:
        BaseGeometry (Class): parent class
    """
    def __init__(self, width, height):
        """__init__ method

        Args:
            width (int): integer type
            height (int): integer type
        """
        self.integer_validator("Rectangle", width)
        self.integer_validator("Rectangle", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area method"""
        return (self.__width * self.__height)

    def __str__(self):
        """__str__ method"""
        return("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """Square class

    Args:
        Rectangle (class): parent class
    """
    def __init__(self, size):
        """__init__ method

        Args:
            size (int): size integer
        """
        self.integer_validator("Square", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """__str__ method"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
