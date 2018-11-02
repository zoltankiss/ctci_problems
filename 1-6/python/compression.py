"""
Compression
"""

def compress(sentence):
    """
    Runtime: O(n).
    """

    new_str = ''
    stored_char = ''
    length = 0

    for char in sentence:
        if length == 0:
            length += 1
            stored_char = char
        elif stored_char != char:
            new_str = _compressed_str(new_str, stored_char, length)
            length = 1
            stored_char = char
        elif stored_char == char:
            length += 1
        else:
            new_str += char

    if stored_char != '':
        new_str = _compressed_str(new_str, stored_char, length)

    return new_str

def _compressed_str(new_str, stored_char, length):
    new_str += stored_char
    if length > 1:
        new_str += str(length)
    return new_str
