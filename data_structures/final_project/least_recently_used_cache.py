from data_structures.linked_lists.double_node import DoubleNode


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend_node(self, node):
        """ Prepend a node to the beginning of the list """
        if self.head is None:
            node.previous = None
            node.next = None
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            node.previous = None
            self.head.previous = node
            self.head = node

    def prepend(self, value):
        """ Prepend a value to the beginning of the list """
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
        else:
            new_head = DoubleNode(value)
            new_head.next = self.head
            self.head.previous = new_head
            self.head = new_head
        return self.head

    def remove_node(self, node):
        """ Remove a node from the list """
        if node.previous is None and node.next is None:
            self.head = None
            self.tail = None
            return
        elif node.previous is None and node.next:
            self.head = node.next
            self.head.previous = None
        elif node.previous and node.next is None:
            self.tail = node.previous
            self.tail.next = None
        else:
            previous_node = node.previous
            next_node = node.next
            previous_node.next = next_node
            next_node.previous = previous_node

    def remove_last(self):
        """ Remove the last node from the list """
        if self.tail is None:
            return
        old_node = self.tail
        self.tail = old_node.previous
        self.tail.next = None
        return old_node


class DoubleLinkedListDict:
    def __init__(self):
        self.keys = DoubleLinkedList()
        self.data = {}

    def push(self, key, value):
        new_node = self.keys.prepend(key)
        self.data[key] = (value, new_node)

    def get(self, key):
        if key in self.data:
            # make key as most recently used item
            value, node = self.data[key]
            self.keys.remove_node(node)
            self.keys.prepend_node(node)
            return value
        return None

    def remove_least_used_el(self):
        least_used_node = self.keys.remove_last()
        key = least_used_node.value
        self.data.pop(key)

    def size(self):
        return len(self.data)


class LRU_Cache:
    def __init__(self, max_size):
        self.cache = DoubleLinkedListDict()
        self.max_size = max_size

    def is_full(self):
        return self.cache.size() == self.max_size

    def get(self, key):
        value = self.cache.get(key)
        if value:
            return value
        return -1

    def set(self, key, value):
        if self.is_full():
            self.cache.remove_least_used_el()
        self.cache.push(key, value)


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
