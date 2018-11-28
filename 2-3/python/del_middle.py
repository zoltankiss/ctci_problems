"""
Find kth to last element
"""

import os
import sys

DIRNAME = os.path.dirname(__file__)
LIBPATH = '/'.join(DIRNAME.split('/')[:-2]) + '/2-0-lib/python'
sys.path.append(LIBPATH)

import linked_lst

def del_middle(node):
    """
    Runtime: O(n).
    """
    next = node.next
    node.data = next.data
    node.next = next.next
