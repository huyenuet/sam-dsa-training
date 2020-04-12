class State:
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def is_visited_left(self):
        return self.visited_left

    def is_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True

    def get_node(self):
        return self.node
