from data_structures.linked_lists.node import Node


class SortedLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """
        Append a value to the Linked List in ascending sorted order

        Args:
           value(int): Value to add to Linked List
        """
        if self.head is None:
            self.head = Node(value)
            return

        if value < self.head.value:
            node = Node(value)
            node.next = self.head
            self.head = node
            return

        if self.head.next is None and value > self.head.value:
            self.head.next = Node(value)
            return

        node = self.head
        while node.next and value >= node.next.value:
            node = node.next

        if node.next is None:
            node.next = Node(value)
        else:
            new_node = Node(value)
            new_node.next = node.next
            node.next = new_node

        return None