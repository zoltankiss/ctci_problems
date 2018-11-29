"""
Unit Tests for problem 1.4.
"""

import unittest
import palindrome_permutation

class TestPalindromePermutation(unittest.TestCase):
    """
    Tests for seeing if a string is a permutation of a palindrome.
    """
    def test_palindrome_permutation(self):
        """
        Test positive case.
        """
        self.assertEqual(palindrome_permutation.palindrome_permutation('xxaab'), True)

    def test_not_palindrome_permutation(self):
        """
        Test negative case.
        """
        self.assertEqual(palindrome_permutation.palindrome_permutation('xxaabc'), False)

if __name__ == '__main__':
    unittest.main()
