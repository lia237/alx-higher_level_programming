#!/usr/bin/python3
""" Creates the Square class """

class Square:
    """ Class representing a square """
    def __init__(self, side_length=0):
        if type(side_length) != int:
            raise TypeError("side_length must be an integer")
        elif side_length < 0:
            raise ValueError("side_length must be >= 0")
        else:
            self.__side_length = side_length

    def area(self):
        return self.__side_length * self.__side_length

