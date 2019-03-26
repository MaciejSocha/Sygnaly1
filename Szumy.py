import random

import numpy as np


class SzumJednostajny:
    def __init__(self, A, t1, d, fp):
        self.A = A  # Amplituda
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału
        self.fp = fp  # Częstotliwość próbkowania

    def x(self):
        return random.uniform(-self.A, self.A)

    def mkTab(self):
        t = self.t1
        xTab = []
        yTab = []
        while t < self.d:
            xTab.append(t)
            yTab.append(self.x())
            t += self.fp
        return xTab, yTab


class SzumGausa:
    def __init__(self, A, t1, d, fp):
        self.A = A  # Amplituda
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału
        self.fp = fp  # Częstotliwość próbkowania

    def x(self):
        tmp = np.random.normal(0, 1/3, 1)
        if tmp > 1.0:
            tmp = 1.0
        elif tmp < -1.0:
            tmp = -1.0
        return self.A * tmp

    def mkTab(self):
        t = self.t1
        xTab = []
        yTab = []
        while t < self.d:
            xTab.append(t)
            yTab.append(self.x())
            t += self.fp
        return xTab, yTab
