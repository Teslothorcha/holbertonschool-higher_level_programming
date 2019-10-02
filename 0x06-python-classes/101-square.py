#!/usr/bin/python3


class Square:

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        p = '#'
        c = self.size
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            while(c):
                for j in range(0, self.position[0]):
                    print(" ", end="")
                print("{}".format(p) * self.size)
                c -= 1

    def __str__(self):
        strr = []
        c = self.size
        if self.__size == 0:
            return ''
        if self.__position[1] >= 0 and self.__position[0] >= 0:
            for s in range(self.__position[1]):
                strr.append('\n')
        while (c):
            for b in range(self.__position[0]):
                strr.append(' ')
            for u in range(self.__size):
                strr.append('#')
            if c != 1:
                strr.append('\n')
            c -= 1
        return ''.join(strr)
