"""
Replace spaces, like in a url.
"""

def space_replace(sentence):
    """
    Runtime: O(n).
    """

    sentence_lst = []

    for char in sentence:
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
            sentence_stack.pop()
            sentence_stack.pop()
            sentence_stack.pop()
            sentence_stack.append(' ')

    return ''.join(sentence_stack)
