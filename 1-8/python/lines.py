"""
Fill in lines
"""

def fill_in(matrix):
    """
    Runtime: O(n^2).
    """

    horizontal = {}
    vertical = {}

    for y, _ in enumerate(matrix):
        for x, _ in enumerate(matrix[0]):
            if matrix[y][x] == 1:
                horizontal[x] = True
                vertical[y] = True

    for y, _ in enumerate(matrix):
        for x, _ in enumerate(matrix[0]):
            if y in vertical:
                matrix[y][x] = 1
            if x in horizontal:
                matrix[y][x] = 1

    return matrix
