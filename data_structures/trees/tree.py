from data_structures.trees.tree_node import Node
from data_structures.queue.double_ended_queue import Queue


class Tree(object):
    def __init__(self, value):
        self.root = Node(value)

    def set_root(self, node):
        self.root = node

    def get_root(self):
        return self.root

    def __repr__(self):
        root = self.root
        level = 0
        queue = Queue()
        queue.enqueue((root, level))
        visit_order = list()

        while not queue.is_empty():
            node, level = queue.dequeue()
            # if node is None: visit_order append a tuple of <empty> placeholder and level
            if node is None:
                visit_order.append(("<empty>", level))
                continue
            else:
                visit_order.append((node, level))
            # if queue has left child: add child and it's level to queue, else, add None to queue
            if node.has_left_child():
                queue.enqueue((node.get_left_child(), level+1))
            else:
                queue.enqueue((None, level+1))
            # if queue has right child: add child and it's level to queue, else, add None to queue
            if node.has_right_child():
                queue.enqueue((node.get_right_child(), level+1))
            else:
                queue.enqueue((None, level+1))

        s = "Tree\n"
        previous_level = -1
        # traverse the visit_order list to get the nodes and placeholders
        for node, level in visit_order:
            # if same level, keep adding node to s
            if level == previous_level:
                s += " | " + str(node)
            # if different level, break the line and add node to s, increase previous level
            else:
                s += "\n" + str(node)
                previous_level += 1
        return s
