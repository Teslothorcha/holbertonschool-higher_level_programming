#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
            self.height = height
            self.width = width
            Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        s = ''
        if self.__width == 0 or self.__height == 0:
            return s
        for c in range(self.__height):
            for f in range(self.__width):
                if f == self.__width - 1 and c != self.__height - 1:
                    s += str(self.print_symbol) + "\n"
                else:
                    s += str(self.print_symbol)
        return s

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_2) == Rectangle.area(rect_1):
            return rect_1
        if Rectangle.area(rect_2) > Rectangle.area(rect_1):
            return rect_2
        if Rectangle.area(rect_2) < Rectangle.area(rect_1):
            return rect_1

    @classmethod
    def square(cls, size=0):
        sq = Rectangle()
        sq.width = size
        sq.height = size
        return sq
