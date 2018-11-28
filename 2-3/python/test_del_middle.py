"""
Unit Tests for problem 2.3.
"""

import unittest
import del_middle

class TestKthElement(unittest.TestCase):
    """
    Delete middle element
    """
    def test_del_middle(self):
        """
        Find kth to last element
        """
        lst = del_middle.linked_lst.LinkedLstNode()
        lst.data = 1
        lst.append_to_tail(2)
        lst.append_to_tail(3)
        lst.append_to_tail(4)
        lst.append_to_tail(5)

        node = lst
        node = node.next
        node = node.next
        del_middle.del_middle(node)

        node = lst
        self.assertEqual(node.data, 1)
        node = node.next
        self.assertEqual(node.data, 2)
        node = node.next
        self.assertEqual(node.data, 4)
        node = node.next
        self.assertEqual(node.data, 5)
        node = node.next
        self.assertEqual(node, None)

if __name__ == '__main__':
    unittest.main()
