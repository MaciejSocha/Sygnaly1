import SygnalyCiagle
import DrawPlot
import Part2.convertAC.Probkowanie as probkowanie

# sygnał do konwersji
signal = SygnalyCiagle.Sinusoidalny(1, 3.14, 0, 10, 0.05)
    # wykres początkowy
xBase, yBase = signal.mkTab()
DrawPlot.normalPlot(xBase, yBase)

# konwersja analogowo-cyfrowa
    # próbkowanie - próbkowanie równomierne
f = 0.2 # częstotliwość próbkowania - w sumie to nie cześtotliwość - do pomyślenia
xPrb, yPrb = probkowanie.probkuj(signal, f)
DrawPlot.discreetPlot(xPrb, yPrb)

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