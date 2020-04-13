from data_structures.trees.tree import Tree
from data_structures.trees.tree_node import Node
from data_structures.queue.double_ended_queue import Queue


# init tree
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


def breadth_first_search(tree: Tree):
    queue = Queue()
    visit_order = list()
    queue.enqueue(tree.get_root())
    while not queue.is_empty():
        node = queue.dequeue()
        visit_order.append(node.get_value())
        if node.has_left_child():
            queue.enqueue(node.get_left_child())
        if node.has_right_child():
            queue.enqueue(node.get_right_child())
    return visit_order


print(breadth_first_search(tree))
