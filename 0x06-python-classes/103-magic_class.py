#!/usr/bin/python3
"""This module peform two operations for a circumference."""
import math


class MagicClass:
    """Magic class that can determine area && circumference of a circle"""

    def __init__(self, radius=0):
        """__init__ method  """
        self.__radius = 0
        if type(self.__radius) is not int and type(self.__radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """area method that determines the area of the circle """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """circumference method determines the circumference of the circle """
        return (2 * math.pi * self.__radius)
