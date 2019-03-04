import os
import sys

DIRNAME = os.path.dirname(__file__)
LIBPATH = '/'.join(DIRNAME.split('/')[:-2]) + '/2-0-lib/python'
sys.path.append(LIBPATH)

import linked_lst

def first_repeating_node(linked_lst):
  ids = {}
  while linked_lst != None:
      if id(linked_lst) in ids:
          return ids[id(linked_lst)]
      ids[id(linked_lst)] = linked_lst
      linked_lst = linked_lst.next
