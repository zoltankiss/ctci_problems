"""
Unit Tests for problem 1.8.
"""

import unittest
import lines

class TestLines(unittest.TestCase):
    """
    Fill in lines.
    """
    def test_lines(self):
        """
        4x4.
        """
        matrix = [
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0]
        ]
        updated_matrix = [
            [1, 1, 1, 1],
            [0, 1, 1, 0],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]

        self.assertEqual(lines.fill_in(matrix), updated_matrix)

if __name__ == '__main__':
    unittest.main()
