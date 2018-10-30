"""
Determine if a string has all unique characters.
"""

def is_unique(val):
    """
    With additional data structures.
    """
    chars = {}
    for char in val:
        if char in chars and chars[char]:
            return False
        chars[char] = True

    return True

def is_unique_no_data_structs(val):
    """
    Without additional data structures.
    """
    for i, chari in enumerate(val):
        for k, chark in enumerate(val):
            if i != k and chari == chark:
                return False

    return True
