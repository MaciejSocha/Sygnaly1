import SygnalyCiagle
import DrawPlot
import Part2.convertAC.Probkowanie as probkowanie
import Part2.convertAC.Kwantyzacja as kwantowanie
import Part2.convertCA.Rekonstrukcja as rekonstrukcja
import Operacje
import Part2.Porownania.MD as MD

# sygnał do konwersji
signal = SygnalyCiagle.Sinusoidalny(1, 1/220, 0, 0.05, 1/44100)
signal2 = SygnalyCiagle.Sinusoidalny(1, 1/30000, 0, 0.001, 1/600000)
# wykres początkowy
print("Robie tablice")
xBase, yBase = signal.mkTab()
xB2, yB2 = signal2.mkTab()
xSum, ySum = Operacje.suma(xBase, yBase, xB2, yB2)
print("Koniec")
DrawPlot.normalPlot(xBase, yBase)
DrawPlot.normalPlot(xB2, yB2)
DrawPlot.normalPlot(xSum, ySum)

# konwersja analogowo-cyfrowa
    # próbkowanie - próbkowanie równomierne
f = 0.05  # częstotliwość próbkowania - w sumie to nie cześtotliwość - do pomyślenia
# xPrb, yPrb = probkowanie.probkuj(signal, f)
xPrb, yPrb = probkowanie.probkujTab(xSum, ySum, f, 0, 0.001, 1/44100)
DrawPlot.discreetPlot(xPrb, yPrb)

    # kwantyzacja - kwnatyzacja równomierna z obcięciem
q = 50  # liość przedziałów kwantyzacji
# xKwt, yKwa = kwantowanie.kwantujTab(xPrb, yPrb, q)
# DrawPlot.discreetPlot(xKwt, yKwa)

# konwersja cyfrowo-analogowa (rekonstrukcja sygnału)
    # rekonstrukcja w opraciu o funkcję sinc
# xRek, yRek = rekonstrukcja.uratuj(xKwt, yKwa, f, 5, 0)
# DrawPlot.normalPlot(xRek, yRek)

# ---------- #
# porównania, ocena konwersji:

# miara podobieństwa sygnałów
    # Maksymalna różnica (MD)
# md = MD.MaximumDif(xBase, yBase, xRek, yRek)
# print("MD:")
# print(md)

# ---------- #
# wykazanie zjawiska aliasingu przy próbokowaniu sygnału
    # dla parametrów f0 = 220Hz, fs=44100Hz znaleźć fd aby zachodziło
