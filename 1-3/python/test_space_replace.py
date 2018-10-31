"""
Unit Tests for problem 1.3.
"""

import unittest
import space_replace

class TestSpaceReplace(unittest.TestCase):
    """
    Tests for replacing spaces.
    """
    def test_space_replace(self):
        """
        Replace spaces, like in a url.
        """
        self.assertEqual(space_replace.space_replace('this is a url'), 'this%20is%20a%20url')

    def test_space_replace_with_extra_whitespace(self):
        """
        Replace spaces, with extra whitespace.
        """
        self.assertEqual(space_replace.space_replace('this is a url    '), 'this%20is%20a%20url')

    def test_inverse_space_replace(self):
        """
        Inverse replace spaces.
        """
        new_string = space_replace.space_replace_inverse('this%20is%20a%20url')

        self.assertEqual(new_string, 'this is a url')

if __name__ == '__main__':
    unittest.main()
