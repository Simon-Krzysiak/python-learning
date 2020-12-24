"""Task:
    You are given an n x n 2D matrix that represents an image. Rotate the
    image by 90 degrees (clockwise).
"""


def rotateImage(matrix):
    length = len(matrix)
    matrix.reverse()

    for i in range(length):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix
