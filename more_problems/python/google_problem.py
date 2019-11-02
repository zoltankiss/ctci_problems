import unittest

def google(str):
    right = ''
    left = ''
    buffer = ''
    strs = []
    started_parsing = False
    parsing_block = False
    for char in str:
        if char == '{' and not parsing_block:
            if right != '':
                strs.append(right.split(','))
                right = ''
            started_parsing = True
            parsing_block = True
        elif char == '}' and parsing_block:
            parsing_block = False
            strs.append(buffer.split(','))
            buffer = ''
        elif parsing_block:
            buffer += char
        elif not started_parsing:
            left += char
        elif not parsing_block:
            right += char
    return add_padding(right, left, combinations(strs))

def add_padding(right, left, lst):
    items = []
    for e in lst:
        items.append(left + e + right)
    return items

def combine(a, b):
    items = []
    for i in a:
        for j in b:
            items.append(i + j)
    return items

def combinations(lst):
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return combine(lst[0], lst[1])
    return combine(lst[0], combinations(lst[1:]))

class TestGoogleProblem(unittest.TestCase):
    def test_one_blocks(self):
        self.assertEqual(google('x{a,b}y'), ['xay', 'xby'])

    def test_two_blocks(self):
        self.assertEqual(google('x{a,b}{1,2}y'), ['xa1y', 'xa2y', 'xb1y', 'xb2y'])

    def test_three_blocks(self):
        self.assertEqual(google('x{a,b}{1,2}{l}y'), ['xa1ly', 'xa2ly', 'xb1ly', 'xb2ly'])

    def test_extra_left_brace(self):
        self.assertEqual(google('x{a{,b}{1,2}y'), ['xa{1y', 'xa{2y', 'xb1y', 'xb2y'])

    def test_block_without_braces(self):
        self.assertEqual(google('x{a,b}1,2{l}y'), ['xa1ly', 'xa2ly', 'xb1ly', 'xb2ly'])

if __name__ == '__main__':
    unittest.main()
