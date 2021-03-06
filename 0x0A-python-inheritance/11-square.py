#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    rectangle class
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)


    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
