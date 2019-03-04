"""
Unit Tests.
"""

import unittest
import loop_detection

class TestLoopDetection(unittest.TestCase):
    def test_returns_start_of_loop(self):
        lst = loop_detection.linked_lst.LinkedLstNode()
        lst.data = 1

        loop = loop_detection.linked_lst.LinkedLstNode()
        loop.data = 5
        loop.next = loop

        lst.next = loop

        self.assertEqual(loop_detection.first_repeating_node(lst), loop)

    def test_loopless_lst(self):
        lst = loop_detection.linked_lst.LinkedLstNode()
        lst.data = 1
        lst.append_to_tail(2)

        self.assertEqual(loop_detection.first_repeating_node(lst), None)

if __name__ == '__main__':
    unittest.main()
