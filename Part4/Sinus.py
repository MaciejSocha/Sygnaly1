import math


def multisinus(t):
    sin1 = math.sin(math.pi * t)
    sin2 = math.sin(2 * math.pi * t)
    sin3 = math.sin((2 * math.pi * t) / 0.5)

    x = (2 * sin1) + sin2 + (5 * sin3)

    return x
