from Nodes import Node

class LinkedList:
    """
    A linked list is a linear data structure where elements are not stored at contiguous
    location. Instead the elements are linked using pointers.

    In a linked list data is stored in nodes and each node is linked to the next and,
    optionally, to the previous. 

    Each node in a list consists of the following parts:

    1) data
    2) A pointer (Or reference) to the next node
    3) Optionally, a pointer to the previous node
    """
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
          if current_node.get_value() != None:
            string_list += str(current_node.get_value()) + "\n"
          current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
          self.head_node = current_node.get_next_node()
        else:
          while current_node:
            next_node = current_node.get_next_node()
            if next_node.get_value() == value_to_remove:
              current_node.set_next_node(next_node.get_next_node())
              current_node = None
            else:
              current_node = next_node
