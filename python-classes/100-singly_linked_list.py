#!usr/bin/python3
"""Creates a class for a node in a linked list and a linked list class.
"""


class Node:
    """Creates a node of a singly linked list.

    Attributes:
        data (int): data the node holds
        next_node: pointer to the next node in the list

    No methods available for single nodes.
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Creates a singly linked list.

    Attributes:
        head: head of linked list. Pointer to the first node.
    """

    def __init__(self):
        self.__head = None

    def __str__(self):
        """Prints a linked list.

        Print all nodes except the last, and returns the
        last node's data as str.

        Return: data of last node as string.
        """
        tmp = self.__head
        if tmp is None:
            return str(None)

        while tmp is not None and tmp.next_node is not None:
            print(tmp.data)
            tmp = tmp.next_node
        return str(tmp.data)

    def sorted_insert(self, value):
        """Inserts a new node in a linked list mantaining the ascending order.

        Attributes:
            values: the value of the node to insert.
        """
        tmp = self.__head
        if tmp is None or tmp.data >= value:
            new = Node(data=value, next_node=tmp)
            self.__head = new

        else:
            while tmp.next_node is not None and tmp.next_node.data <= value:
                tmp = tmp.next_node

            next_ptr = tmp.next_node
            new = Node(data=value, next_node=next_ptr)
            tmp.next_node = new
