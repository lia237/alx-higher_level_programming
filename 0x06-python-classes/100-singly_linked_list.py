#!/usr/bin/python3
"""Class for Node"""
class Node:
    """ Defines a node of a singly linked list
        Attributes:
            value (int): data
            next_node (Node, optional): node
    """

    def __init__(self, value, next_node=None):
        """Initialize Node
        args:
            value (int): data stored in node
            next_node (Node): next node
        """
        self.value = value
        self.next_node = next_node

    @property
    def value(self):
        """Value getter
        returns:
            value (int)
        """
        return self.__value

    @value.setter
    def value(self, val):
        """Value setter
        args:
            val (int): value to set
        returns:
            None
        """
        if not isinstance(val, int):
            raise TypeError("Value must be an integer")
        self.__value = val

    @property
    def next_node(self):
        """Next node getter
        returns:
            next_node (Node)
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        """Next node setter
        args:
            node (Node): node to set
        returns:
            None
        """
        if not isinstance(node, Node) and node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = node


class SinglyLinkedList:
    """Singly linked list class
    """

    def __init__(self):
        """Initialize linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert node in correct sorted position
        args:
            value (int): value for new node
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.value > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                   tmp.next_node.value < value):
                tmp = tmp.next_node

            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.value))
            tmp = tmp.next_node
        return '\n'.join(values)

