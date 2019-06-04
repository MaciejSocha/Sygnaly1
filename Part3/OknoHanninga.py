import math


def hanning(n, M):
    w = 0.5 - (0.5 * math.cos((2*n*math.pi)/M))
    return w
