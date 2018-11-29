"""
Find kth to last element
"""

import os
import sys

DIRNAME = os.path.dirname(__file__)
LIBPATH = '/'.join(DIRNAME.split('/')[:-2]) + '/2-0-lib/python'
sys.path.append(LIBPATH)

import linked_lst

def kth_element(lst, k):
    """
    Runtime: O(n).
    """

    length = 0
    lst_pointer = lst

    while lst_pointer is not None:
        length += 1
        lst_pointer = lst_pointer.next

    lst_pointer_result = lst

    for _ in range(1, length - k):
        lst_pointer_result = lst_pointer_result.next

    return lst_pointer_result.data
