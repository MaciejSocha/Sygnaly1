import math


def matrixVector(matrix, vector):
    ret = [0] * vector.__len__()
    for x in range(matrix.__len__()):
        for y in range(vector.__len__()):
            a = matrix[y][x]
            b = vector[y][0]
            ret[x] += (a * b)
        ret[x] *= 1 / math.sqrt(2)

    return ret
