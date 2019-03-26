import numpy as np
import math


class ImpulsJednostkowy:
    def __init__(self, A, ns, n1, d, f):
        self.A = A  # Amplituda
        self.ns = ns  # Numer próbki dla której następuje skok
        self.n1 = n1  # Numer pierwszej próbki
        self.d = d  # Czas trwania sygnału
        self.f = f  # Częstość próbkowania

    def x(self, n):
        if n == self.ns:
            return self.A
        else:
            return 0

    def mkTab(self):
        n = self.n1
        xTab = []
        yTab = []
        while n < self.d:
            xTab.append(n)
            yTab.append(self.x(round(n/self.f)))
            n += self.f
        return xTab, yTab

    def wrSr(self):
        n2 = self.n1 + self.d
        r = 1 / (n2 - self.n1 + 1)
        n = self.n1
        suma = 0
        while n < n2:
            suma = self.x(n)
            n += self.f
        return r * suma

    def wrSrBzw(self):
        n2 = self.n1 + self.d
        r = 1 / (n2 - self.n1 + 1)
        n = self.n1
        suma = 0
        while n < n2:
            suma = math.fabs(self.x(n))
            n += self.f
        return r * suma

    def mcSr(self):
        n2 = self.n1 + self.d
        r = 1 / (n2 - self.n1 + 1)
        n = self.n1
        suma = 0
        while n < n2:
            suma = math.pow(self.x(n), 2)
            n += self.f
        return r * suma

    def wr(self):
        n2 = self.n1 + self.d
        r = 1 / (n2 - self.n1 + 1)
        n = self.n1
        suma = 0
        while n < n2:
            suma = math.pow((self.x(n) - self.wrSr()), 2)
            n += self.f
        return r * suma

    def wrSk(self):
        n2 = self.n1 + self.d
        r = 1 / (n2 - self.n1 + 1)
        n = self.n1
        suma = 0
        while n < n2:
            suma = math.pow(self.x(n), 2)
            n += self.f
        return math.sqrt(r * suma)


class SzumImpulsowy:
    def __init__(self, A, t1, d, f, p):
        self.A = A  # Amplituda
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału
        self.f = f  # Częstotliwość próbkowania
        self.p = p  # Prawdopodobieństwo wystąpienia wartości A

    def x(self):
        aa = []
        aa.append(self.A)
        aa.append(0)
        pp = []
        pp.append(self.p)
        pp.append(1-self.p)
        return np.random.choice(aa, None, False, pp)

    def mkTab(self):
        t = self.t1
        xTab = []
        yTab = []
        while t < self.d:
            xTab.append(t)
            yTab.append(self.x())
            t += self.f
        return xTab, yTab

    def wrSr(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = self.x()
            n += self.f
        return r * suma

    def wrSrBzw(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = math.fabs(self.x())
            n += self.f
        return r * suma

    def mcSr(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = math.pow(self.x(), 2)
            n += self.f
        return r * suma

    def wr(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = math.pow((self.x() - self.wrSr()), 2)
            n += self.f
        return r * suma

    def wrSk(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = math.pow(self.x(), 2)
            n += self.f
        return math.sqrt(r * suma)
