import math


class SygnalCiagly:
    def __init__(self, A, T, t1, d, fp):
        self.A = A  # Amplituda
        self.T = T  # Okres podstawowy
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału
        self.fp = fp  # Częstotliwość próbkowania

    def x(self, t):
        raise NotImplementedError("nie ta")

    def mkTab(self):
        t = self.t1
        xTab = []
        yTab = []
        while t < self.d:
            xTab.append(t)
            yTab.append(self.x(t))
            t += self.fp
        return xTab, yTab

    def wrSr(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        n2 = math.floor(n2/self.T)
        while n < n2:
            suma = self.x(n)
            n += self.fp
        return r * suma

    def wrSrBzw(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        n2 = math.floor(n2 / self.T)
        while n < n2:
            suma = math.fabs(self.x(n))
            n += self.fp
        return r * suma

    def mcSr(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        n2 = math.floor(n2 / self.T)
        while n < n2:
            suma = math.pow(self.x(n), 2)
            n += self.fp
        return r * suma

    def wr(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        n2 = math.floor(n2 / self.T)
        while n < n2:
            suma = math.pow((self.x(n) - self.wrSr()), 2)
            n += self.fp
        return r * suma

    def wrSk(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        n2 = math.floor(n2 / self.T)
        while n < n2:
            suma = math.pow(self.x(n), 2)
            n += self.fp
        return math.sqrt(r * suma)
