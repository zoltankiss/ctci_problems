"""
Rm dups
"""

import os
import sys

DIRNAME = os.path.dirname(__file__)
LIBPATH = '/'.join(DIRNAME.split('/')[:-2]) + '/2-0-lib/python'
sys.path.append(LIBPATH)

import linked_lst

def rm_dups(lst):
    """
    Runtime: O(n).
    """

    dups = {}
    prev = None
    lst_pointer = lst

    while lst_pointer is not None:
        if lst_pointer.data in dups:
            prev.next = lst_pointer.next
        else:
            dups[lst_pointer.data] = True
            prev = lst_pointer
        lst_pointer = lst_pointer.next
    return lst

def rm_dups_without_hash(lst):
    """
    Runtime: O(n^2).
    """

    lst_pointer = lst

    while lst_pointer is not None:
        runner = lst_pointer.next
        prev = lst_pointer
        while runner is not None:
            if lst_pointer.data == runner.data:
                prev.next = runner.next
            prev = runner
            runner = runner.next
        lst_pointer = lst_pointer.next

    return lst
