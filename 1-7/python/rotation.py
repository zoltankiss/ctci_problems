"""
Rotation
"""

def rotate(matrix):
    """
    Runtime: O(n^2).
    """

    for k in range(0, (len(matrix) // 2)):
        submatrix_len = len(matrix) - 1 - (k * 2)
        for i in range(0, submatrix_len):
            tmp = matrix[k][i + k]
            matrix[k][i + k] = matrix[submatrix_len - i + k][k]
            matrix[submatrix_len - i + k][k] = matrix[submatrix_len + k][submatrix_len - i + k]
            matrix[submatrix_len + k][submatrix_len - i + k] = matrix[i + k][submatrix_len + k]
            matrix[i + k][submatrix_len + k] = tmp

    return matrix
