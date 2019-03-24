import unittest
import queue_by_stacks

class TestQueueByStacks(unittest.TestCase):
    def test_queue_by_stacks(self):
        queue = queue_by_stacks.MyQueue()
        queue.push(1)
        queue.push(2)

        self.assertEqual(queue.pop(), 1)
        self.assertEqual(queue.pop(), 2)

if __name__ == '__main__':
    unittest.main()
