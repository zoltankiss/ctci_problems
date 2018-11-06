"""
Unit Tests for problem 1.7.
"""

import unittest
import rotation

class TestCompression(unittest.TestCase):
    """
    rotation.
    """
    def test_rotation(self):
        """
        5x5.
        """
        matrix = [
            [1, 2, 3, 4, 5],
            [16, 1, 2, 3, 6],
            [15, 8, 3, 4, 7],
            [14, 7, 6, 5, 8],
            [13, 12, 11, 10, 9]
        ]
        rotated_matrix = [
            [13, 14, 15, 16, 1],
            [12, 7, 8, 1, 2],
            [11, 6, 3, 2, 3],
            [10, 5, 4, 3, 4],
            [9, 8, 7, 6, 5]
        ]

        self.assertEqual(rotation.rotate(matrix), rotated_matrix)

    def test_simple_rotation(self):
        """
        2x2.
        """
        matrix = [
            [1, 2],
            [3, 4]
        ]
        rotated_matrix = [
            [3, 1],
            [4, 2]
        ]

        self.assertEqual(rotation.rotate(matrix), rotated_matrix)

    def test_nine_by_nine_rotation(self):
        """
        3x3.
        """
        matrix = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ]
        rotated_matrix = [
            [7, 8, 1],
            [6, 9, 2],
            [5, 4, 3]
        ]

        self.assertEqual(rotation.rotate(matrix), rotated_matrix)

if __name__ == '__main__':
    unittest.main()
