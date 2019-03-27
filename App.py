import SygnalyDyskretne
import SygnalyCiagle
import Szumy
import DrawPlot
import SaveLoad
import Operacje

#Sygnały sinusoidalne
#parametry:
# A - amplituda
# T - okres podstawowy
# t1 - chwila początkowa
# d - chwila końcowa
# fp - częstotliwość próbkowania
sigSin = SygnalyCiagle.Sinusoidalny(1, 3.14, 0, 10, 0.05)
sinSinJedno = SygnalyCiagle.SinusoidalnyWyprostowanyJednopolowkowo(1, 3.14, 0, 10, 0.05)
sigSinDwu = SygnalyCiagle.SinusoidalnyWyprostowanyDwupolowkowo(1, 3.14, 0, 10, 0.05)
#Sygnały Prostokątne/trójkątne
# parametry:
# A - amplituda
# T - okres podstawowy
# t1 - chwila początkowa
# d - chwila końcowa
# kw - współczynnik wypełnienia
# fp - częstotliwość próbkowania
sigProsto = SygnalyCiagle.Prostokatny(1, 2, 0, 10, 0.5, 0.05)
sigProstoSym = SygnalyCiagle.ProstokatnySymetryczny(1, 2, 0, 10, 0.5, 0.05)
sigTroj = SygnalyCiagle.Trojkatny(1, 2, 0, 10, 0.5, 0.05)
#Skok jednostkowy
#parametry:
# A - amplituda
# t1 - chwila początkowa
# d - chwila końcowa
# ts - czwila skoku
# fp - częstotliwośc próbkowania
sigSkok = SygnalyCiagle.SkokJednostkowy(1, 0, 10, 5, 0.05)
#Szum o rozkładizie jednostajnym i Gaussa
# parametry:
# A - amplituda
# t1 - chwila początkowa
# d - chwila końcowa
# fp - częstoliwośc próbkowania
sigJedno = Szumy.SzumJednostajny(0.25, 0, 10, 0.05)
sigGauss = Szumy.SzumGausa(0.25, 0, 10, 0.05)
# impuls jednostkowy
# parametry:
# A - amplituda
# ns - próbka na której nasßepuje skok
# n1 - chwila początkowa
# d  - chwila końcowa
# fp - częstotliwośc próbek
sigDysJedno = SygnalyDyskretne.ImpulsJednostkowy(1, 5, 0, 5, 0.2)
# szum impulsowy
# parametry
# A - amplituda
# n1 - chwila początkowa
# d - chwila końcowa
# fp - częstotliwość probkowania
# p - prawdopodobieństwo wystąpienia skoku
sigDysSzum = SygnalyDyskretne.SzumImpulsowy(1, 0, 5, 0.2, 0.2)

# Generownie podstawowych sygnałów
x1, y1 = sigSin.mkTab()
x2, y2 = sigProstoSym.mkTab()

# Rysowanie wykresów
DrawPlot.normalPlot(x1, y1)
DrawPlot.normalPlot(x2, y2)

# Operacje na sygnałach
# xrez, yrez = Operacje.suma(x1, y1, x2, y2)

# DrawPlot.normalPlot(xrez, yrez)

# Zapis/Odczyt z plików
# SaveLoad.save(xrez, yrez, "flie1.txt")

# xload, yload = SaveLoad.load("file1.txt")

# DrawPlot.normalPlot(xload, yload)
