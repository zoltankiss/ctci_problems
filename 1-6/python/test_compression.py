"""
Unit Tests for problem 1.6.
"""

import unittest
import compression

class TestCompression(unittest.TestCase):
    """
    Compress strings.
    """
    def test_compression(self):
        """
        Test replacement.
        """
        self.assertEqual(compression.compress('aaabbbb'), 'a3b4')

    def test_when_compression_is_not_helpful(self):
        """
        Test negative case.
        """
        self.assertEqual(compression.compress('abc'), 'abc')

if __name__ == '__main__':
    unittest.main()
