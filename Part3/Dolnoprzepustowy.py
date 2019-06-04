import math as np

import DrawPlot
from Part3 import OknoHanninga


def low_filter(M, K):
    impulseResponseValues = []
    x = []
    for n in range(M):
        if n == (M - 1) / 2:
            x.append(n)
            impulseResponseValues.append(2.0 / K)
        else:
            impulseResponseValues.append(
                np.sin((2.0 * np.pi * (n - (M - 1.0) / 2.0)) / K) / (np.pi * (n - (M - 1.0) / 2.0)))
            x.append(n)
    # DrawPlot.normalPlot(x, impulseResponseValues)
    newTab = []
    for n in range(len(impulseResponseValues)):
        newTab.append(OknoHanninga.hanning(n, M) * impulseResponseValues[n])

    return newTab


def low_high_filter(M, K):
    impulseResponseValues = []
    signal = low_filter(M, K)

    for n in range(len(signal)):
        impulseResponseValues.append(signal[n] * 2 * np.sin(np.pi * n / 2))

    return impulseResponseValues
