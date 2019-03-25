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
        self.d = d  # Czas trwania sygnału


class SinusoidalnyWyprostowanyDwupolowkowo:
    def __init__(self, A, T, t1, d):
        self.A = A  # Amplituda
        self.T = T  # Okres podstawowy
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału


class Prostokatny:
    def __init__(self, A, T, t1, d, kw):
        self.A = A  # Amplituda
        self.T = T  # Okres podstawowy
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału
        self.kw = kw  # Współczynnik wypełnienia


class ProstokatnySymetryczny:
    def __init__(self, A, T, t1, d, kw):
        self.A = A  # Amplituda
        self.T = T  # Okres podstawowy
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału
        self.kw = kw  # Współczynnik wypełnienia


class Trojkatny:
    def __init__(self, A, T, t1, d, kw):
        self.A = A  # Amplituda
        self.T = T  # Okres podstawowy
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału
        self.kw = kw  # Współczynnik wypełnienia


class SkokJednostkowy:
    def __init__(self, A, t1, d, ts):
        self.A = A  # Amplituda
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału
        self.ts = ts  # TODO
