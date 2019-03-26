import numpy as np


def wartoscSrednia():
    return 0


def wartoscSredniaBezwzgledna():
    return 0


def wartoscSkuteczna():
    return 0


def wariancja():
    return 0


def mocSrednia():
    return 0


class ImpulsJednostkowy:
    def __init__(self, A, ns, n1, l, f):
        self.A = A  # Amplituda TODO not implemented
        self.ns = ns  # Numer próbki dla której następuje skok
        self.n1 = n1  # Numer pierwszej próbki TODO not implemented
        self.l = l  # TODO
        self.f = f  # Częstość próbkowania TODO not implemented

    def x(self, n):
        if n == self.ns:
            return 1
        else:
            return 0


class SzumImpulsowy:
    def __init__(self, A, t1, d, f, p):
        self.A = A  # Amplituda
        self.t1 = t1  # Czas początkowy TODO not implemented
        self.d = d  # Czas trwania sygnału TODO not implemented
        self.f = f  # Częstotliwość próbkowania TODO not implemented
        self.p = p  # Prawdopodobieństwo wystąpienia wartości A

    def x(self, n):
        aa = []
        aa.append(self.A)
        aa.append(0)
        pp = []
        pp.append(self.p)
        pp.append(1-self.p)
        return np.random.choice(aa, None, False, pp)
