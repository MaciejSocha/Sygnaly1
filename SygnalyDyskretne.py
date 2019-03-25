class ImpulsJednostkowy:
    def __init__(self, A, ns, n1, l, f):
        self.A = A  # Amplituda
        self.ns = ns  # Numer próbki dla której następuje skok
        self.n1 = n1  # Numer pierwszej próbki
        self.l = l  # TODO
        self.f = f  # Częstość próbkowania


class SzumImpulsowy:
    def __init__(self, A, t1, d, f, p):
        self.A = A  # Amplituda
        self.t1 = t1  # Czas początkowy
        self.d = d  # Czas trwania sygnału
        self.f = f  # Częstotliwość próbkowania
        self.p = p  # Prawdopodobieństwo wystąpienia wartości A
