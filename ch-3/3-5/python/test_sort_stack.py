import unittest
import sort_stack

class TestSortStack(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(sort_stack.SortStack().sort(sort_stack.Stack([5, 3, 4, 9])).lst, [9, 5, 4, 3])

if __name__ == '__main__':
    unittest.main()
