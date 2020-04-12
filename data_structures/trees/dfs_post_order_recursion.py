from data_structures.trees.tree import Tree
from data_structures.trees.tree_node import Node


# init tree
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


def dfs_post_order_recursion(tree: Tree):
    visit_list = list()
    node = tree.get_root()

    # traverse
    def traverse(node):
        if node:
            # traverse left
            traverse(node.get_left_child())

            # traverse right
            traverse(node.get_right_child())

            # visit the node
            visit_list.append(node.get_value())

    traverse(node)

    return visit_list


print(dfs_post_order_recursion(tree))
