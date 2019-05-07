
def test():
    print("Hello")


def probkuj(sygnal, f):
    print("Próbkuje sygnały")
    xTab = []
    yTab = []
    t = sygnal.t1
    while t < sygnal.d:
        yTab.append(sygnal.x(t * f))
        xTab.append(t)
        t += 1
    return xTab, yTab
