import math
import DrawPlot


def sinc(x):
    if x == 0:
        return 1
    else:
        return math.sin(x* math.pi) / (x*math.pi)


def sincPlot(start, end, krok):
    xTab = []
    yTab = []
    while start < end:
        xTab.append(start)
        yTab.append(sinc(start))
        start += krok
    DrawPlot.normalPlot(xTab, yTab)


def uratuj(xTab, yTab, f, d, t0):  # TODO no to nie działa poprawie, ale sprawia pozory xD
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
