from data_structures.trees.tree import Tree
from data_structures.trees.tree_node import Node
from data_structures.trees.state import State
from data_structures.stack.stack_linkedlist import Stack


# init tree
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


def dfs_pre_order(tree: Tree):
    visit_list = list()
    stack = Stack()

    # start with root node, visit it and add it to the stack
    node = tree.get_root()
    state = State(node)
    stack.push(state)
    visit_list.append(node.get_value())

    while node:

        if node.has_left_child() and not state.is_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            state = State(node)
            stack.push(state)
            visit_list.append(node.get_value())
        elif node.has_right_child() and not state.is_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            state = State(node)
            stack.push(state)
            visit_list.append(node.get_value())
        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.peek()
                node = state.get_node()
            else:
                node = None
    return visit_list


print(dfs_pre_order(tree))
