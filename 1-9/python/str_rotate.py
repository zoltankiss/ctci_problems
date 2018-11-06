"""
Str Rotation
"""

def is_rotated(stringa, stringb):
    """
    Runtime: O(k).
    """

    return stringa in stringb + stringb
