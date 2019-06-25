import matplotlib.pyplot as plt
import SygnalyCiagle
import Szumy
import SygnalyDyskretne
import DrawPlot as plot
import Operacje
import math
import SaveLoad

# plt.plot([1, 2, 3, 4])
# plt.show()
from Part4.Fourier import DFT
from Part4.Fourier import FFT

print("Hello")
# inp = input("Enter:")
# print(inp)

# sig = SygnalyCiagle.Trojkatny(1, 10, 0, 50, 0.3, 0.1)
# sig = Szumy.SzumGausa(5, 0, 20, 0.05)
# sig = SygnalyCiagle.Trojkatny(1, 1, 0, 5, 0.75, 0.05)

fp = 1000
fs = 10
deltaT = 1.0/fp
T = 1/fs
A = 1
duration = 10




# sig = SygnalyDyskretne.SzumImpulsowy(1, 0, 50, 1, 0.5)
sig = SygnalyCiagle.Sinusoidalny(A, T, 0, duration, deltaT)
sig2 = SygnalyCiagle.Sinusoidalny(A, T*2, 0, duration,deltaT)
xTab, yTab = sig.mkTab()
x2, y2 = sig2.mkTab()
sumax,sumay =Operacje.suma(xTab,yTab,x2,y2)

N = len(xTab)

f0 = 1/(deltaT*N)
f01 = fp/N
# sig2 = SygnalyCiagle.Prostokatny(1, 15, 0, 30, 0.5, 0.2)


X, Y, Yi, Ymod = DFT(sumax, sumay, 300)

for x in range(len(X)):
    X[x] *= f0
# xTab2, yTab2 = sig2.mkTab()
plot.FourierMod(X, Ymod)
plot.FourierComplexPlot(X, Y, Yi)



