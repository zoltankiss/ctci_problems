import os
import sys

DIRNAME = os.path.dirname(__file__)
LIBPATH = '/'.join(DIRNAME.split('/')[:-2]) + '/2-0-lib/python'
sys.path.append(LIBPATH)

import linked_lst

def partition(lst, k):
    partitioned_lst_start = linked_lst.LinkedLstNode()
    partitioned_lst_end = linked_lst.LinkedLstNode()
    partitioned_lst_middle = linked_lst.LinkedLstNode()

    while lst is not None:
        if lst.data < k:
            _append_to_potentially_empty_lst(partitioned_lst_start, lst.data)
        if lst.data == k:
            _append_to_potentially_empty_lst(partitioned_lst_middle, lst.data)
        if lst.data > k:
            _append_to_potentially_empty_lst(partitioned_lst_end, lst.data)
        lst = lst.next

    while partitioned_lst_middle is not None:
        partitioned_lst_start.append_to_tail(partitioned_lst_middle.data)
        partitioned_lst_middle = partitioned_lst_middle.next

    while partitioned_lst_end is not None:
        partitioned_lst_start.append_to_tail(partitioned_lst_end.data)
        partitioned_lst_end = partitioned_lst_end.next

    return partitioned_lst_start

def _append_to_potentially_empty_lst(lst, data):
    if lst.length() == 1 and lst.data is None:
        lst.data = data
    else:
        lst.append_to_tail(data)
