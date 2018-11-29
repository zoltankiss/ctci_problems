"""
See if a string can be transformed into another
in one operation (char replacement, deletion, insertion)
"""

def is_one_op_away(sentence1, sentence2):
    """
    Runtime: O(n).
    """

    chars1 = list(sentence1)
    chars2 = list(sentence2)

    while _has_elems(chars1, chars2) and chars1[0] == chars2[0]:
        del chars1[0]
        del chars2[0]

    while _has_elems(chars1, chars2) and chars1[-1] == chars2[-1]:
        del chars1[-1]
        del chars2[-1]

    return len(chars1) <= 1 and len(chars2) <= 1

def _has_elems(chars1, chars2):
    return len(chars1) > 0 and len(chars2) > 0
