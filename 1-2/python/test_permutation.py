"""
Unit Tests for problem 1.2.
"""

import unittest
import permutation

class TestIsPermutation(unittest.TestCase):
    """
    Tests for ``Permutation``.
    """
    def test_is_permutation(self):
        """
        If a string is a permutation of another.
        """
        self.assertEqual(permutation.is_permutation('god', 'dog'), True)

    def test_is_not_permutation(self):
        """
        If a string is not a permutation of another.
        """
        self.assertEqual(permutation.is_permutation('god', 'cat'), False)

if __name__ == '__main__':
    unittest.main()
