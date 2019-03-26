import random
import math
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

    def wrSr(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = self.x()
            n += self.fp
        return r * suma

    def wrSrBzw(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = math.fabs(self.x())
            n += self.fp
        return r * suma

    def mcSr(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = math.pow(self.x(), 2)
            n += self.fp
        return r * suma

    def wr(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = math.pow((self.x() - self.wrSr()), 2)
            n += self.fp
        return r * suma

    def wrSk(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = math.pow(self.x(), 2)
            n += self.fp
        return math.sqrt(r * suma)


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

    def wrSr(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = self.x()
            n += self.fp
        return r * suma

    def wrSrBzw(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = math.fabs(self.x())
            n += self.fp
        return r * suma

    def mcSr(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = math.pow(self.x(), 2)
            n += self.fp
        return r * suma

    def wr(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = math.pow((self.x() - self.wrSr()), 2)
            n += self.fp
        return r * suma

    def wrSk(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = math.pow(self.x(), 2)
            n += self.fp
        return math.sqrt(r * suma)
