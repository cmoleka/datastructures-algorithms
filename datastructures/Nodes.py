class Node:
    """
    Nodes are the fundamental building blocks of many computer science data structures.
    They form the basis for linked lists, stacks, queues, trees, and more.

    An individual node contains data and links to other nodes.
    Each data structure adds additional constraints or behavior to these features
    to create the desired structure.
    """
    def __init__(self, value, previous_node=None, next_node=None):
        self.value = value
        self.previous_node = previous_node
        self.next_node = next_node

    """
        set_previous_node: sets the previous_node.
    """
    def set_previous_node(self, previous_node):
        self.previous_node = previous_node

    """
        set_next_node: sets the next_node.
    """
    def set_next_node(self, next_node):
        self.next_node = next_node

    """
        get_previous_node: Returns  previous_node.
    """
    def get_previous_node(self):
        return self.previous_node

    """
        get_next_node: Returns  next_node.
    """
    def get_next_node(self):
        return self.next_node

    """
        get_value: Returns value of the Node.
    """
    def get_value(self):
        return self.value

    """
        show: Displays the node as a {dict}
    """
    def show(self):
        node_info = {
             "value": self.value,
             "previous_node": self.previous_node,
             "next_node": self.next_node
             }
        return print(node_info)
        
