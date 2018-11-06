"""
Unit Tests for problem 1.9.
"""

import unittest
import str_rotate

class TestStrRotation(unittest.TestCase):
    """
    TestStrRotation.
    """
    def test_is_rotated(self):
        """
        test_is_rotated.
        """
        self.assertEqual(str_rotate.is_rotated('isrotated', 'rotatedis'), True)

    def test_is_not_rotated(self):
        """
        test_is_not_rotated.
        """
        self.assertEqual(str_rotate.is_rotated('isrotatxd', 'rotatedis'), False)

if __name__ == '__main__':
    unittest.main()
