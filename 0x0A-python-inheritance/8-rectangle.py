#!/usr/bin/python3
class BaseGeometry():
    """
    base class
    """
    def area(self):
        """
        method that raises an error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rwctangle class inherited from basegeomtry
    """
    def __init__(self, width, height):
        """
        initilize rectangle object validatin values with father method
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
