"""
Tests for seeing if a string is a permutation of a palindrome.
"""

def palindrome_permutation(sentence):
    """
    Runtime: O(n).

    A sentence is a permutation of a palindrome if
    and only if the number of odd-number appearing chars it contains
    is no greater than one.
    """

    chars_freq = _string_chars_freq(sentence)

    odd_number_chars = 0

    for _, val in chars_freq.items():
        if not val % 2 == 0:
            odd_number_chars += 1
        if odd_number_chars > 1:
            return False

    return True


def _string_chars_freq(string):
    chars = {}

    for char in string:
        if char in chars.keys():
            chars[char] += 1
        else:
            chars[char] = 1

    return chars
