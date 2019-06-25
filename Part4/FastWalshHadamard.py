import numpy
from scipy.linalg import hadamard
import math

from Part4 import MatrixMultiplication


def fwht(a):
    """In-place Fast Walsh-Hadamard Transform of array a"""
    h = 1
    while h < len(a):
        for i in range(0, len(a), h * 2):
            for j in range(i, i + h):
                x = a[j]
                y = a[j + h]
                a[j] = x + y
                a[j + h] = x - y
        h *= 2

    return a


def fast(tabX, tab):
    pow2 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
    w = 0
    nb = tab.__len__()
    print(nb)
    if nb in pow2:
        w = nb
    else:
        i = 0
        while i < 13:
            if pow2[i] < nb < pow2[i + 1]:
                w = pow2[i + 1]
            i += 1
    print(w)
    diff = w - nb
    print(tabX)
    it = tabX.__len__()
    itt = tabX[it - 1]
    for x in range(diff):
        itt += 0.0625
        tab.append(0)
        tabX.append(itt)

    # Main part
    hd = hadamard(w)
    newtab = [[0 for x in range(1)] for y in range(w)]
    for x in range(nb - 1):
        newtab[x][0] = tab[x]

    uptab = [[0 for x in range(1)] for y in range(math.floor(w / 2))]
    downtab = [[0 for x in range(1)] for y in range(math.floor(w / 2))]

    for i in range(math.floor(w / 2)):
        uptab[i][0] = (tab[i] + tab[math.floor(w / 2) + i])
        downtab[i][0] = (tab[i] - tab[math.floor(w / 2) + i])

    # * hadamond

    for x in range(pow2.__len__()):
        if w == pow2[x]:
            previous = pow2[x-1]

    hd = hadamard(previous)
    newup = MatrixMultiplication.matrixVector(hd, uptab)
    newdown = MatrixMultiplication.matrixVector(hd, downtab)
    # end this

    rettab = newup + newdown
    # rt = []
    # for x in range(rettab.__len__()):
       # rt.append(rettab[x][0])

    return tabX, rettab
