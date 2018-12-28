import unittest
import partition

class TestPartition(unittest.TestCase):
    def test_del_middle(self):
        lst = partition.linked_lst.LinkedLstNode()
        lst.data = 10
        lst.append_to_tail(1)
        lst.append_to_tail(5)
        lst.append_to_tail(2)
        lst.append_to_tail(3)

        partitioned_lst = partition.partition(lst, 3)

        node = partitioned_lst
        self.assertTrue(node.data <= 3)
        node = node.next
        self.assertTrue(node.data <= 3)
        node = node.next
        self.assertTrue(node.data == 3)
        node = node.next
        self.assertTrue(node.data >= 3)
        node = node.next
        self.assertTrue(node.data >= 3)

if __name__ == '__main__':
    unittest.main()
