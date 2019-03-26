import math


class Sinusoidalny:
    def __init__(self, A, T, t1, d, fp):
        self.A = A  # Amplituda
        self.T = T  # Okres podstawowy
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału
        self.fp = fp  # Częstotliwość próbkowania

    def x(self, t):
        return self.A * math.sin(((2 * math.pi) / self.T) * (t - self.t1))

    def mkTab(self):
        t = self.t1
        xTab = []
        yTab = []
        while t < self.d:
            xTab.append(t)
            yTab.append(self.x(t))
            t += self.fp
        return xTab, yTab


class SinusoidalnyWyprostowanyJednopolowkowo:
    def __init__(self, A, T, t1, d, fp):
        self.A = A  # Amplituda
        self.T = T  # Okres podstawowy
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału
        self.fp = fp  # Częstotliwość próbkowania

    def x(self, t):
        return 0.5 * self.A * (math.sin(((2 * math.pi) / self.T) * (t - self.t1)) + math.fabs(
            math.sin(((2 * math.pi) / self.T) * (t - self.t1))))

    def mkTab(self):
        t = self.t1
        xTab = []
        yTab = []
        while t < self.d:
            xTab.append(t)
            yTab.append(self.x(t))
            t += self.fp
        return xTab, yTab


class SinusoidalnyWyprostowanyDwupolowkowo:
    def __init__(self, A, T, t1, d, fp):
        self.A = A  # Amplituda
        self.T = T  # Okres podstawowy
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału
        self.fp = fp  # Częstotliwość próbkowania

    def x(self, t):
        return self.A * math.fabs(math.sin(((2 * math.pi) / self.T) * (t - self.t1)))

    def mkTab(self):
        t = self.t1
        xTab = []
        yTab = []
        while t < self.d:
            xTab.append(t)
            yTab.append(self.x(t))
            t += self.fp
        return xTab, yTab


class Prostokatny:
    def __init__(self, A, T, t1, d, kw, fp):
        self.A = A  # Amplituda
        self.T = T  # Okres podstawowy
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału
        self.kw = kw  # Współczynnik wypełnienia
        self.fp = fp  # Częstotliwość próbkowania

    def x(self, t):
        return self.A * (t % self.T < (self.kw * self.T))

    def mkTab(self):
        t = self.t1
        xTab = []
        yTab = []
        while t < self.d:
            xTab.append(t)
            yTab.append(self.x(t))
            t += self.fp
        return xTab, yTab


class ProstokatnySymetryczny:
    def __init__(self, A, T, t1, d, kw, fp):
        self.A = A  # Amplituda
        self.T = T  # Okres podstawowy
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału
        self.kw = kw  # Współczynnik wypełnienia
        self.fp = fp  # Częstotliwość próbkowania

    def x(self, t):
        if self.A * (t % self.T < (self.kw * self.T)):
            return self.A
        else:
            return -self.A

    def mkTab(self):
        t = self.t1
        xTab = []
        yTab = []
        while t < self.d:
            xTab.append(t)
            yTab.append(self.x(t))
            t += self.fp
        return xTab, yTab


class Trojkatny:
    def __init__(self, A, T, t1, d, kw, fp):
        self.A = A  # Amplituda
        self.T = T  # Okres podstawowy
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału
        self.kw = kw  # Współczynnik wypełnienia
        self.fp = fp  # Częstotliwość próbkowania

    def x(self, t):
        if self.A * (t % self.T < (self.kw * self.T)):
            return (self.A / (self.kw * self.T)) * (t - (math.floor(t / self.T)) * self.T - self.t1)
        else:
            return (-self.A / (self.T * (1 - self.kw))) * (t - (math.floor(t / self.T)) * self.T - self.t1) + (
                            self.A / (1 - self.kw))

    def mkTab(self):
        t = self.t1
        xTab = []
        yTab = []
        while t < self.d:
            xTab.append(t)
            yTab.append(self.x(t))
            t += self.fp
        return xTab, yTab


class SkokJednostkowy:
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
