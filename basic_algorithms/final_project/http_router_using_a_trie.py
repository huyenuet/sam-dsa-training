from collections import defaultdict


class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children and a handler
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler

    def insert(self, node):
        return self.children[node]


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with a root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, nodes, handler):
        current_node = self.root

        for node in nodes:
            current_node = current_node.insert(node)

        current_node.handler = handler

    def find(self, nodes):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        if nodes == [""]:
            return self.root.handler

        for node in nodes:
            if node not in current_node.children:
                return None
            current_node = current_node.children[node]

        return current_node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler):
        # Create a new RouteTrie for holding our routes
        self.router = RouteTrie(handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        path_elements = self.split_path(path)
        self.router.insert(path_elements, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        path_elements = self.split_path(path)
        handler = self.router.find(path_elements)
        if handler is None:
            return "not found handler"
        return handler

    def split_path(self, path):
        path_elements = path.split("/")
        if path.endswith("/"):
            return path_elements[:-1]
        return path_elements


# create the router and add 2 routes
router = Router("root handler")
router.add_handler("/home/", "home handler")  # add a route
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'home handler'
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler'
print(router.lookup("/home/about/me"))  # should print 'not found handler'
