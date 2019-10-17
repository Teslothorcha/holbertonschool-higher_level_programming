#!/usr/bin/python3
class Student():
        def __init__(self, first_name, last_name, age):
                self.first_name = first_name
                self.last_name = last_name
                self.age = age

        def to_json(self, attrs=None):
                d = {}
                if type(attrs) is list:
                        s = attrs[:]
                        for c in range(len(attrs)):
                                if attrs[c] in self.__dict__:
                                        d.setdefault(s[c], self.__dict__[s[c]])
                        return d
                else:
                        return self.__dict__
