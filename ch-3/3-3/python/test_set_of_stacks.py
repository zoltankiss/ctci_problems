import unittest
import set_of_stacks

class TestSetOfStacks(unittest.TestCase):
    def test_three_stacks(self):
        stacks = set_of_stacks.SetOfStacks(2)
        stacks.push(0)
        stacks.push(1)
        stacks.push(2)
        stacks.push(3)
        for stack in stacks.stacks:
            self.assertTrue(len(stack) <= stacks.stack_max_len)

        self.assertEqual(stacks.pop(), 3)
        self.assertEqual(stacks.pop(), 2)
        self.assertEqual(stacks.pop(), 1)
        self.assertEqual(stacks.pop(), 0)

if __name__ == '__main__':
    unittest.main()
