"""
Unit Tests for problem 1.5.
"""

import unittest
import replacement

class TestReplacement(unittest.TestCase):
    """
    See if a string can be transformed into another
    in one operation (char replacement, deletion, insertion)
    """
    def test_replacement(self):
        """
        Test replacement.
        """
        self.assertEqual(replacement.is_one_op_away('aabbcc', 'aadbcc'), True)

    def test_deletion(self):
        """
        Test deletion.
        """
        self.assertEqual(replacement.is_one_op_away('aabbcc', 'aabcc'), True)

    def test_insertion(self):
        """
        Test insertion.
        """
        self.assertEqual(replacement.is_one_op_away('aabbcc', 'aabbbcc'), True)

    def test_not_replacement(self):
        """
        Test negative case.
        """
        self.assertEqual(replacement.is_one_op_away('aabbcc', 'aaddcc'), False)

if __name__ == '__main__':
    unittest.main()
