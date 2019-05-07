import SygnalyCiagle
import DrawPlot

# sygnał do konwersji
signal = SygnalyCiagle.Sinusoidalny(1, 3.14, 0, 10, 0.05)
    # wykres początkowy
x, y = signal.mkTab()
DrawPlot.normalPlot(x, y)

# konwersja analogowo-cyfrowa
    # próbkowanie - próbkowanie równomierne

    # kwantyzacja - kwnatyzacja równomierna z obcięciem

# konwersja cyfrowo-analogowa (rekonstrukcja sygnału)
    # rekonstrukcja w opraciu o funkcję sinc


# ---------- #
# porównania, ocena konwersji:

# miara podobieństwa sygnałów
    # Maksymalna różnica (MD)


# ---------- #
# wykazanie zjawiska aliasingu przy próbokowaniu sygnału
    # dla parametrów f0 = 220Hz, fs=44100Hz znaleźć fd aby zachodziło