"""
Unit Tests for problem 2.1.
"""

import unittest
import rm_dups

class TestRmDupsFromLinkedLst(unittest.TestCase):
    """
    TestRmDupsFromLinkedLst.
    """
    def test_rm_dups_from_linked_lst(self):
        """
        Rm from a linked lst.
        """
        lst = rm_dups.linked_lst.LinkedLstNode()
        lst.data = 1
        lst.append_to_tail(2)
        lst.append_to_tail(2)
        lst.append_to_tail(3)
        lst.append_to_tail(3)

        lst = rm_dups.rm_dups(lst)

        self.assertEqual(lst.data, 1)
        self.assertEqual(lst.next.data, 2)
        self.assertEqual(lst.next.next.data, 3)

    def test_rm_dups_without_hash(self):
        """
        Rm from a linked lst.
        """
        lst = rm_dups.linked_lst.LinkedLstNode()
        lst.data = 1
        lst.append_to_tail(2)
        lst.append_to_tail(2)
        lst.append_to_tail(3)
        lst.append_to_tail(3)

        lst = rm_dups.rm_dups_without_hash(lst)

        self.assertEqual(lst.data, 1)
        self.assertEqual(lst.next.data, 2)
        self.assertEqual(lst.next.next.data, 3)

if __name__ == '__main__':
    unittest.main()
