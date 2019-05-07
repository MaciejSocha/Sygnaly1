import math


def sinc(x):
    if x == 0:
        return 1
    else:
        return math.sin(x) / (x)


def uratuj(xTab, yTab, f, d, t0):
    print("Rekonstrukcja")
    xRet = []
    yRet = []
    t = t0
    while t < d:
        sum = 0
        n = 0
        while n < len(yTab):
            sum += yTab[n] * sinc((t/f) - n)
            n += 1
        xRet.append(t)
        yRet.append(sum)
        t += f
    return xRet, yRet
