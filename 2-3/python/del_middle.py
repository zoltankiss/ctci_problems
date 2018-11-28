import os
import sys

DIRNAME = os.path.dirname(__file__)
LIBPATH = '/'.join(DIRNAME.split('/')[:-2]) + '/2-0-lib/python'
sys.path.append(LIBPATH)

import linked_lst

def del_middle(node):
    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next
