import SygnalyCiagle
import DrawPlot
import Part2.convertAC.Probkowanie as probkowanie
import Part2.convertAC.Kwantyzacja as kwantowanie
import Part2.convertCA.Rekonstrukcja as rekonstrukcja

# sygnał do konwersji
signal = SygnalyCiagle.Sinusoidalny(3, 3, 0, 20, 0.01)
    # wykres początkowy
xBase, yBase = signal.mkTab()
DrawPlot.normalPlot(xBase, yBase)

# konwersja analogowo-cyfrowa
    # próbkowanie - próbkowanie równomierne
f = 0.4  # częstotliwość próbkowania - w sumie to nie cześtotliwość - do pomyślenia
xPrb, yPrb = probkowanie.probkuj(signal, f)
# DrawPlot.discreetPlot(xPrb, yPrb)

    # kwantyzacja - kwnatyzacja równomierna z obcięciem
q = 5  # liość przedziałów kwantyzacji
xKwt, yKwa = kwantowanie.kwantujTab(xPrb, yPrb, q)
# DrawPlot.discreetPlot(xKwt, yKwa)

# konwersja cyfrowo-analogowa (rekonstrukcja sygnału)
    # rekonstrukcja w opraciu o funkcję sinc
xRek, yRek = rekonstrukcja.uratuj(xKwt, yKwa, f, 20, 0)
DrawPlot.normalPlot(xRek, yRek)

# ---------- #
# porównania, ocena konwersji:

# miara podobieństwa sygnałów
    # Maksymalna różnica (MD)


# ---------- #
# wykazanie zjawiska aliasingu przy próbokowaniu sygnału
    # dla parametrów f0 = 220Hz, fs=44100Hz znaleźć fd aby zachodziło
