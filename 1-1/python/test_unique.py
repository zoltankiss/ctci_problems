"""
Unit Tests for problem 1.1.
"""

import unittest
import unique

class TestUnique(unittest.TestCase):
    """
    Tests for ``Unique``.
    """
    def test_unique(self):
        """
        No duplicates.
        """
        self.assertEqual(unique.is_unique('abcde'), True)

    def test_has_duplicate_chars(self):
        """
        Has duplicates.
        """
        self.assertEqual(unique.is_unique('abccde'), False)

    def test_empty_string(self):
        """
        Empty String.
        """
        self.assertEqual(unique.is_unique(''), True)

    def test_unique_no_data_structs(self):
        """
        No duplicates without additional data structures.
        """
        self.assertEqual(unique.is_unique_no_data_structs('abcde'), True)

    def test_has_duplicate_chars_no_data_structs(self):
        """
        Has duplicates without additional data structures.
        """
        self.assertEqual(unique.is_unique_no_data_structs('abccde'), False)

    def test_empty_string_no_data_structs(self):
        """
        Empty String without additional data structures.
        """
        self.assertEqual(unique.is_unique_no_data_structs(''), True)

if __name__ == '__main__':
    unittest.main()
