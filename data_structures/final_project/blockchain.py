import hashlib
from datetime import datetime

from data_structures.linked_lists.node import Node


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, value):
        """ Append a node to the end of the linked list """
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def find_last_node_value(self):
        """ Search the linked list for a node with the requested value and return the node. """
        if self.head is None:
            return None

        node = self.head
        while node.next:
            node = node.next

        return node.value


class Blockchain:
    def __init__(self, data):
        timestamp = datetime.utcnow()
        self.blockchain = LinkedList(Block(timestamp, data, None))

    def insert(self, data):
        last_block = self.blockchain.find_last_node_value()
        previous_hash = last_block.hash
        timestamp = datetime.utcnow()
        new_block = Block(timestamp, data, previous_hash)
        self.blockchain.append(new_block)


block_chain = Blockchain("root")
block_chain.insert("child 1")
block_chain.insert("child 2")
block_chain.insert("child 3")
