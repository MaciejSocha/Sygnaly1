import Part2.convertAC.Probkowanie as Prb
import math


def kwantujTab(xTab, yTab, q):
    print("Kwantyzacja")
    sigMax = max(yTab)
    sigMin = min(yTab)
    szerokoscPrzedzialu = (sigMax - sigMin) / q
    krancePrzedzialow = []
    krancePrzedzialow.append(sigMin)
    tmp = sigMin
    while tmp < sigMax:
        krancePrzedzialow.append((tmp + szerokoscPrzedzialu))
        tmp += szerokoscPrzedzialu
    j = 0
    for y in yTab:
        i = 1
        mini = math.fabs(krancePrzedzialow[0] - yTab[i])
        miniIndex = 0
        while i < len(krancePrzedzialow):
            if math.fabs(krancePrzedzialow[i] - y) < mini:
                mini = math.fabs(krancePrzedzialow[i] - y)
                miniIndex = krancePrzedzialow[i]
            i += 1
        yTab[j] = miniIndex
        j += 1
    return xTab, yTab


# jednocześnie próbkuje i kwantuje
def kwantujSig(signal, f, q):
    print("Kwantyzacja")
    x, y = Prb.probkuj(signal, f)
    xRez, yRez = kwantujTab(x, y, q)
    return xRez, yRez
