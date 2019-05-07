import math


def probkuj(sygnal, f):
    print("Próbkuje sygnały")
    xTab = []
    yTab = []
    t = sygnal.t1
    while t < sygnal.d:
        yTab.append(sygnal.x(t))
        xTab.append(t)
        t += f
    print("Koniec")
    return xTab, yTab


def probkujTab(xT, yT, f, t1, d, fp):
    print("Próbkuje sygnały")
    xTab = []
    yTab = []
    t = t1
    l = round(fp/f)
    while t < d and l < len(yT):
        yTab.append(yT[l])
        xTab.append(t)
        t += f
        l += 1
    print("Koniec")
    return xTab, yTab
