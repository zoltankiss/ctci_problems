"""
Linked List Implementations
"""

class LinkedLstNode:
    """
    Single Linked List
    """
    def __init__(self):
        self.next = None
        self.data = None

    def append_to_tail(self, data):
        """
        Add element to end.
        """
        tail_node = self
        while tail_node.next is not None:
            tail_node = tail_node.next
        tail_node.next = LinkedLstNode()
        tail_node.next.data = data

    def print_linked_list(lst):
        lst_pointer = lst
        while lst_pointer != None:
            print(lst_pointer.data)
            lst_pointer = lst_pointer.next
