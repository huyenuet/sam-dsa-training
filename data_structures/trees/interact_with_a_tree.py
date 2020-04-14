from data_structures.trees.tree import Tree
from data_structures.trees.tree_node import Node


# init tree
tree = Tree(1)
tree.insert_with_loop(2)
tree.insert_with_loop(3)
tree.insert_with_loop(5)
tree.insert_with_loop(4)
tree.insert_with_loop(0)
print(tree)

print("\n=====================")
tree = Tree(1)
tree.insert_with_recursion(2)
tree.insert_with_recursion(3)
tree.insert_with_recursion(5)
tree.insert_with_recursion(4)
tree.insert_with_recursion(0)
print(tree)


print("\n=====================")
print(tree.search(0))
print(tree.search(10))

print("\n=delete a node ====================")
tree = Tree(5)
tree.insert_with_recursion(3)
tree.insert_with_recursion(4)
tree.insert_with_recursion(7)
tree.insert_with_recursion(6)
tree.insert_with_recursion(10)
tree.insert_with_recursion(9)
tree.insert_with_recursion(8)
tree.insert_with_recursion(8.5)
print(tree)
tree.delete(4)
print(tree)
tree.delete(7)
print(tree)
tree.delete(9)
print(tree)
