#!/usr/bin/python3
"""
Class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square
    manager that inherits
    from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string info"""
        s1 = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        s2 = " - {}".format(self.size)
        return s1 + s2

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """square updater"""
        la = ['id', 'size', 'x', 'y']
        if args is not None and len(args) != 0:
            for b in range(len(args)):
                setattr(self, la[b], args[b])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """gets dictionary"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
