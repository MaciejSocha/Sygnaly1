import DrawPlot
import Operacje
import SygnalyCiagle
from Part3 import Splot, OknoHanninga, Dolnoprzepustowy

print("Test")
tabX1 = [0, 1, 2, 3]
tabY1 = [1, 2, 3, 4]
tabX2 = [0, 1, 2]
tabY2 = [5, 6, 7]

x, y = Splot.SplotDyskretny(tabX1, tabY1, tabX2, tabY2)
print(x)
print(y)
x, y = Splot.SplotDyskretny(tabX2, tabY2, tabX1, tabY1)
print(x)
print(y)


tabx = []
taby = []

for x in range(25):
    tabx.append(x)
    taby.append(OknoHanninga.hanning(x, 25))

# DrawPlot.normalPlot(tabx, taby)

sig1 = SygnalyCiagle.Prostokatny(1, 5, 0, 20, 0.5, 0.01)
sig2 = SygnalyCiagle.Sinusoidalny(1, 1, 0, 5, 0.01)

x1 = []
x2 = []
y1 = []
y2 = []

x1, y1 = sig1.mkTab()
x2, y2 = sig2.mkTab()

x, y = Splot.SplotDyskretny(x1, y1, x1, y1)

DrawPlot.normalPlot(x1, y1)
#DrawPlot.normalPlot(x2, y2)
#DrawPlot.normalPlot(x, y)

M = 63
K = 3.65

odp = Dolnoprzepustowy.low_high_filter(M, K)

xs, ys = Splot.SplotDyskretny(x1, odp, x1, y1)

DrawPlot.normalPlot(xs, ys)
