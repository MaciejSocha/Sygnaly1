
def test():
    print("Hello")


def probkuj(sygnal, f):
    print("Próbkuje sygnały")
    xTab = []
    yTab = []
    t = sygnal.t1
    while t < sygnal.d:
        yTab.append(sygnal.x(t))
        xTab.append(t)
        t += f
    return xTab, yTab
