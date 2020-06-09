class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):

        # TODO: Return True if the value is in the tree, return False otherwise.
        if self.root is None:
            return False
        return self.preorder_search(self.root, find_val)

    def print_tree(self):

        # TODO: Print out all tree nodes as they are visited in a pre-order traversal.

        return False

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        if start.value == find_val:
            return True
        elif find_val < start.value:
            if start.left:
                return self.preorder_search(start.left, find_val)
            return False
        elif find_val > start.value:
            if start.right:
                return self.preorder_search(start.right, find_val)
            return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
print("Pass" if tree.search(4) else "Fail")
print("Pass" if not tree.search(6) else "Fail")
# print ("Pass" if (tree.print_tree() == '1-2-4-5-3') else "Fail")
