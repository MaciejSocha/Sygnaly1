import numpy
from scipy.linalg import hadamard
import math

from Part4 import MatrixMultiplication

print(hadamard(256))


def calc(tabX, tab):
    pow2 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
    w = 0
    nb = tab.__len__()

    if nb in pow2:
        w = nb
    else:
        i = 0
        while i < 13:
            if pow2[i] < nb < pow2[i + 1]:
                w = pow2[i + 1]
            i += 1

    diff = w - nb

    it = tabX.__len__()
    itt = tabX[it-1]
    for x in range(diff):
        itt += 0.0625
        tab.append(0)
        tabX.append(itt)

    # Main part
    hd = hadamard(w)
    newtab = [[0 for x in range(1)] for y in range(w)]
    for x in range(nb-1):
        newtab[x][0] = tab[x]

    nt = numpy.asanyarray(newtab)
    tabret = MatrixMultiplication.matrixVector(hd, nt)
    return tabX, tabret
