import math
import SygnalyCiagleBase as baza


class Sinusoidalny(baza.SygnalCiagly):
    def __init__(self, A, T, t1, d, fp):
        super().__init__(A, T, t1, d, fp)

    def x(self, t):
        return self.A * math.sin(((2 * math.pi) / self.T) * (t - self.t1))


class SinusoidalnyWyprostowanyJednopolowkowo(baza.SygnalCiagly):
    def __init__(self, A, T, t1, d, fp):
        super().__init__(A, T, t1, d, fp)

    def x(self, t):
        return 0.5 * self.A * (math.sin(((2 * math.pi) / self.T) * (t - self.t1)) + math.fabs(
            math.sin(((2 * math.pi) / self.T) * (t - self.t1))))


class SinusoidalnyWyprostowanyDwupolowkowo(baza.SygnalCiagly):
    def __init__(self, A, T, t1, d, fp):
        super().__init__(A, T, t1, d, fp)

    def x(self, t):
        return self.A * math.fabs(math.sin(((2 * math.pi) / self.T) * (t - self.t1)))


class Prostokatny(baza.SygnalCiagly):
    def __init__(self, A, T, t1, d, kw, fp):
        super().__init__(A, T, t1, d, fp)
        self.kw = kw  # Współczynnik wypełnienia

    def x(self, t):
        return self.A * (t % self.T < (self.kw * self.T))


class ProstokatnySymetryczny(baza.SygnalCiagly):
    def __init__(self, A, T, t1, d, kw, fp):
        super().__init__(A, T, t1, d, fp)
        self.kw = kw  # Współczynnik wypełnienia

    def x(self, t):
        if self.A * (t % self.T < (self.kw * self.T)):
            return self.A
        else:
            return -self.A


class Trojkatny(baza.SygnalCiagly):
    def __init__(self, A, T, t1, d, kw, fp):
        super().__init__(A, T, t1, d, fp)
        self.kw = kw  # Współczynnik wypełnienia

    def x(self, t):
        if self.A * (t % self.T < (self.kw * self.T)):
            return (self.A / (self.kw * self.T)) * (t - (math.floor(t / self.T)) * self.T - self.t1)
        else:
            return (-self.A / (self.T * (1 - self.kw))) * (t - (math.floor(t / self.T)) * self.T - self.t1) + (
                            self.A / (1 - self.kw))


class SkokJednostkowy():
    def __init__(self, A, t1, d, ts, fp):
        self.A = A  # Amplituda
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału
        self.ts = ts  # Skok
        self.fp = fp  # Częstotliwość próbkowania

    def x(self, t):
        if t < self.ts:
            return 0
        elif t == self.ts:
            return 0.5 * self.A
        else:
            return self.A

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
        while n < n2:
            suma = self.x(n)
            n += self.fp
        return r * suma

    def wrSrBzw(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = math.fabs(self.x(n))
            n += self.fp
        return r * suma

    def mcSr(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = math.pow(self.x(n), 2)
            n += self.fp
        return r * suma

    def wr(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = math.pow((self.x(n) - self.wrSr()), 2)
            n += self.fp
        return r * suma

    def wrSk(self):
        n2 = self.t1 + self.d
        r = 1 / (n2 - self.t1 + 1)
        n = self.t1
        suma = 0
        while n < n2:
            suma = math.pow(self.x(n), 2)
            n += self.fp
        return math.sqrt(r * suma)
