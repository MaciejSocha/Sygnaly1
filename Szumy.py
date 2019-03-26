import random

import numpy as np


class SzumJednostajny:
    def __init__(self, A, t1, d):
        self.A = A  # Amplituda
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału

    def x(self, t):
        if t < self.t1:
            return 0
        else:
            return random.uniform(-self.A, self.A)


class SzumGausa:
    def __init__(self, A, t1, d):
        self.A = A  # Amplituda
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału

    def x(self, t):
        tmp = np.random.normal(0, 1/3, 1)
        if tmp > 1.0:
            tmp = 1.0
        elif tmp < -1.0:
            tmp = -1.0
        return self.A * tmp
