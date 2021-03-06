"""
Replace spaces, like in a url.
"""

def space_replace(sentence):
    """
    Runtime: O(n).
    """

    sentence_lst = []
    chars = list(sentence)

    while chars[-1] == ' ':
        chars.pop()

    for char in chars:
        if char == ' ':
            sentence_lst.append('%20')
        else:
            sentence_lst.append(char)

    return ''.join(sentence_lst)

def space_replace_inverse(sentence):
    """
    Runtime: O(n). A little more interesting than #space_replace
    """

    sentence_stack = []
    space = []

    for char in sentence:
        sentence_stack.append(char)
        if space + [char] in (['%'], ['%', '2'], ['%', '2', '0']):
            space.append(char)
        else:
            space = []
        if len(space) == 3:
            for _ in range(0, 3):
                sentence_stack.pop()
            sentence_stack.append(' ')

    return ''.join(sentence_stack)
