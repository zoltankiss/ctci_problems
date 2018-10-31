"""
Determine if a string is a permutation of another.
"""

def is_permutation(str1, str2):
    """
    Runtime: O(n).
    """
    chars1 = _string_chars_freq(str1)
    chars2 = _string_chars_freq(str2)

    for key, val in chars1.items():
        if not key in chars2:
            return False
        if chars2[key] != val:
            return False

    return True

def _string_chars_freq(string):
    chars = {}

    for char in string:
        if char in chars.items():
            chars[char] += 1
        else:
            chars[char] = 0

    return chars
