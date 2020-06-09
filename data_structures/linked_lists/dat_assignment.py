class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, max_size=20):
        self.max_size = max_size
        self.size = 0
        self.head = None
        for i in range(0, max_size):
            self.append("FF")

    def prepend(self, value):
        """ Prepend a node to the beginning of the list """

        if self.head is None:
            self.head = Node(value)
            return
        if self.is_full():
            return
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        self.size += 1

    def append(self, value):
        """ Append a node to the end of the list """

        if self.head is None:
            self.head = Node(value)
            return
        if self.is_full():
            return
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        if self.head is None:
            return None

        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next

        raise ValueError("Value not found in the list.")

    def remove(self, value):
        """ Delete the first node with the desired data. """
        if value < 0 or value > 100:
            print("Value is invalid")
            return

        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next

        raise ValueError("Value not found in the list.")

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next

        return node.value

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        if pos == 0:
            self.prepend(value)
            return

        index = 0
        node = self.head
        while node.next and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return

            index += 1
            node = node.next
        else:
            self.append(value)

    def get_size(self):
        """ Return the size or length of the linked list. """
        return self.size

    def is_full(self):
        return self.max_size == self.size

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def print_all_items(self):
        if self.get_size() == 0:
            print("Linked List is empty")
            return
        node = self.head
        while node.next:
            print(node)
            node = node.next
