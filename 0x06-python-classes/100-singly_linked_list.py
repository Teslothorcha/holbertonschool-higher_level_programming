#!/usr/bin/python3


class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        printt = ""
        while temp is not None:
            printt += str(temp.data)
            printt += "\n"
            temp = temp.next_node
        printt = printt[:len(printt) - 1]
        return printt

    def sorted_insert(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        if self.head is None:
            self.head = Node(value)
            return

        temp = self.head
        if temp.data > value:
            new = Node(value, temp)
            self.head = new
            return

        while temp.next_node is not None:
            if temp.next_node.data > value:
                new = Node(value, temp.next_node)
                temp.next_node = new
                return
            temp = temp.next_node

        temp.next_node = Node(value)
