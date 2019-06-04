import math as np

from Part3 import OknoHanninga


def low_filter(M, fo, fs):
    impulseResponseValues = []
    for n in range(M):
        if n == (M - 1) / 2:
            impulseResponseValues.append(2.0 * fo / fs)
        else:
            impulseResponseValues.append(
                np.sin(2.0 * np.pi * (n - (M - 1.0) / 2.0) * fo / fs) / (np.pi * (n - (M - 1.0) / 2.0)))
    newTab = []
    for n in range(len(impulseResponseValues)):
        newTab.append(OknoHanninga.hanning(n, M) * impulseResponseValues[n])

    return newTab
