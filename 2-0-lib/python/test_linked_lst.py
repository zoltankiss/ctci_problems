"""
Unit Tests.
"""

import unittest
import linked_lst

class TestLinkedLst(unittest.TestCase):
    """
    TestLinkedLst.
    """
    def test_lst(self):
        """
        Test functions.
        """
        lst = linked_lst.LinkedLstNode()
        lst.data = 1
        lst.append_to_tail(2)
        lst.append_to_tail(3)

        self.assertEqual(lst.data, 1)
        self.assertEqual(lst.next.data, 2)
        self.assertEqual(lst.next.next.data, 3)
        self.assertEqual(lst.next.next.next, None)

if __name__ == '__main__':
    unittest.main()
