def check_binary_search_tree(node, lower, upper):
    """
    Determine whether the input is a binary tree or not

    Args:
       node(Tree): A BST object
    Returns:
       bool: True if it is a BST and False if not
    """
    # An empty tree is BST
    if node is None:
        return True

    # False if this node violates lower/upper constraint
    if node.value < lower or node.value > upper:
        return False

    # Otherwise check the subtrees recursively
    # tightening the lower or upper constraint
    return (check_binary_search_tree(node.left, lower, node.value - 1) and
            check_binary_search_tree(node.right, node.value + 1, upper))


class Tree:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return str(self.value)


f = Tree(4)
e = Tree(3, None, f)
d = Tree(1)
b = Tree(2, d, e)
c = Tree(6)
a = Tree(5, b, c)

my_tree = a

lower = 0
upper = 100

print("Pass" if check_binary_search_tree(my_tree, lower, upper) else "Fail")

d = Tree(1)
e = Tree(4)
a = Tree(2, d, e)
f = Tree(5)
b = Tree(3, a, f)
my_tree = b
print("Pass" if not check_binary_search_tree(my_tree, lower, upper) else "Fail")
