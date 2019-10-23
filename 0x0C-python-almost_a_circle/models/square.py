#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        s1 = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        s2 = " - {}".format(self.size)
        return s1 + s2

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        la = ['id', 'size', 'x', 'y']
        if args is not None and len(args) != 0:
            for b in range(len(args)):
                setattr(self, la[b], args[b])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
