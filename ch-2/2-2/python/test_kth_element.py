"""
Unit Tests for problem 2.2.
"""

import unittest
import kth_element

class TestKthElement(unittest.TestCase):
    """
    Find kth to last element
    """
    def test_kth_element(self):
        """
        Find kth to last element
        """
        lst = kth_element.linked_lst.LinkedLstNode()
        lst.data = 1
        lst.append_to_tail(2)
        lst.append_to_tail(3)
        lst.append_to_tail(4)
        lst.append_to_tail(5)

        self.assertEqual(kth_element.kth_element(lst, 1), 4)

if __name__ == '__main__':
    unittest.main()
