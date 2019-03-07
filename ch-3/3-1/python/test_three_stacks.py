import unittest
import three_stacks

class TestThreeStacks(unittest.TestCase):
    def test_three_stacks(self):
        stacks = three_stacks.ThreeStacks()
        stacks.push(0, 2)
        stacks.push(0, 3)
        stacks.push(1, 1)
        stacks.push(2, 0)

        self.assertEqual(stacks.pop(0), 3)
        self.assertEqual(stacks.pop(0), 2)
        self.assertEqual(stacks.pop(1), 1)
        self.assertEqual(stacks.pop(2), 0)

if __name__ == '__main__':
    unittest.main()
