import math

class Sinusoidalny:
    def __init__(self, A, T, t1, d):
        self.A = A  # Amplituda
        self.T = T  # Okres podstawowy
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału TODO not implemented

    def x(self, t):
        return self.A * math.sin(((2 * math.pi) / self.T) * (t - self.t1))


class SinusoidalnyWyprostowanyJednopolowkowo:
    def __init__(self, A, T, t1, d):
        self.A = A  # Amplituda
        self.T = T  # Okres podstawowy
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału TODO not implemented

    def x(self, t):
        return 0.5 * self.A * (math.sin(((2 * math.pi) / self.T) * (t - self.t1)) + math.fabs(math.sin(((2 * math.pi) / self.T) * (t - self.t1))))


class SinusoidalnyWyprostowanyDwupolowkowo:
    def __init__(self, A, T, t1, d):
        self.A = A  # Amplituda
        self.T = T  # Okres podstawowy
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału TODO not implemented

    def x(self, t):
        return self.A * math.fabs(math.sin(((2 * math.pi)/self.T) * (t - self.t1)))


class Prostokatny:
    def __init__(self, A, T, t1, d, kw):
        self.A = A  # Amplituda
        self.T = T  # Okres podstawowy
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału TODO not implemented
        self.kw = kw  # Współczynnik wypełnienia

    def x(self, t):
        if t < self.t1:
            return 0
        else:
            return self.A * (t % self.T < (self.kw * self.T))



class ProstokatnySymetryczny:
    def __init__(self, A, T, t1, d, kw):
        self.A = A  # Amplituda
        self.T = T  # Okres podstawowy
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału TODO not implemented
        self.kw = kw  # Współczynnik wypełnienia

    def x(self, t):
        if t < self.t1:
            return 0
        else:
            if self.A * (t % self.T < (self.kw * self.T)):
                return self.A
            else:
                return -self.A


class Trojkatny:
    def __init__(self, A, T, t1, d, kw):
        self.A = A  # Amplituda
        self.T = T  # Okres podstawowy
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału TODO not implemented
        self.kw = kw  # Współczynnik wypełnienia

    def x(self, t):
        return 0  # TODO not implement


class SkokJednostkowy:
    def __init__(self, A, t1, d, ts):
        self.A = A  # Amplituda
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału TODO not implemented
        self.ts = ts  # Skok

    def x(self, t):
        if t < self.t1 or t < self.ts:
            return 0
        elif t == self.ts:
            return 0.5 * self.A
        else:
            return self.A
