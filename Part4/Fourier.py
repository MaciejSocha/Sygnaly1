import math
import numpy as np

def DFT(xTab,yTab,M):
    YTab = []
    YiTab = []
    XTab = []
    YmodTab = []
    N = len(xTab)
    for m in range(0,M):
        sum = 0
        sumi = 0
        for n in range(0,N):
            x, xi = Euler(m,n,N)
            sum += yTab[n]*x
            sumi += yTab[n]*(-xi)
        sum /= N
        sumi /= N
        YTab.append(sum)
        YiTab.append(sumi)
        XTab.append(m)
        YmodTab.append(math.sqrt(pow(sum,2)+pow(sumi,2)))
    return XTab, YTab, YiTab, YmodTab


def Euler(m, n, N):
    x = math.cos(((2*math.pi*m*n)/N))
    xi = math.sin(((2*math.pi*m*n)/N))
    return x, xi


def DFT_slow(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


def FFT(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 32:  # this cutoff should be optimized
        return DFT_slow(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:N / 2] * X_odd,
                               X_even + factor[N / 2:] * X_odd])



