class Tree:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return str(self.value)


def find_binary_tree_height(node):
    """
    Find the height of a binary tree

    Args:
       tree(object): Input binary tree
    Returns:
       int: The height of the tree
    """

    if node is None:
        return 0
    else:
        return 1 + max(find_binary_tree_height(node.left), find_binary_tree_height(node.right))


f = Tree("F")
e = Tree("E", None, f)

d = Tree("D")
b = Tree("B", d, e)

c = Tree("C")
a = Tree("A", b, c)

my_tree = a

print("Pass" if (4 == find_binary_tree_height(my_tree)) else "Fail")
