from data_structures.trees.tree_node import Node


class Tree(object):
    def __init__(self, value):
        self.root = Node(value)

    def set_root(self, node):
        self.root = node

    def get_root(self):
        return self.root
