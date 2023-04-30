#!/usr/bin/python3

"""100-singly_linked_list.py
This module contains a class Node that defines a node of a singly linked list:
by:

- Private instance attribute: data:
    - property def data(self): to retrieve it
    - property setter def data(self, value): to set it:
        - data must be an integer, otherwise raise a TypeError exception with
            the message data must be an integer
- Private instance attribute: next_node:
    - property def next_node(self): to retrieve it
    - property setter def next_node(self, value): to set it:
        - next_node can be None or must be a Node, otherwise raise a TypeError
          exception with the message next_node must be a Node object
- Instantiation with data and next_node:
    def __init__(self, data, next_node=None):
"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Sets attributes for a Node object when it is instanciated

        Args:
            data (int): Content of node
            next_node (Node): Next node in list
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """property method

        Returns:
            (int) - Content of node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """setter method

        Args:
            value (int): Value to set for the content of the node
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """property method

        Returns:
            (Node) - Next node in list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter method

        Args:
            value (Node): Value to set for the next_node
        """
        if isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Sets attributes for a Node object when it is instanciated"""
        self.__head = None

    def __str__(self):
        """Sets print value for SinglyLinkedList object"""
        list_str = ""
        node = self.__head
        while (node is not None):
            list_str += str(node.data)
            node = node.next_node
            if node is not None:
                list_str += '\n'
        return list_str

    def sorted_insert(self, value):
        """Inserts a node in the linked list, in ascending order

        Args:
            value (int): Value for new node
        """
        node = self.__head
        if node is None:
            self.__head = Node(value)
        elif node.data >= value:
            self.__head = Node(value, self.__head)
        else:
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            node.next_node = Node(value, node.next_node)
