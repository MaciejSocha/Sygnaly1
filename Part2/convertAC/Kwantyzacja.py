import Part2.convertAC.Probkowanie as Prb


def kwantujTab(xTab, yTab, q):
    print("Kwantyzacja")
    x = []
    y = []

    return x, y


# jednocześnie próbkuje i kwantuje
def kwantujSig(signal, f, q):
    print("Kwantyzacja")
    xRez = []
    yRez = []
    x, y = Prb.probkuj(signal, f)
    xRez, yRez = kwantujTab(x, y, q)
    return xRez, yRez
