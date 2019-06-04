import DrawPlot
from Part3 import Splot, OknoHanninga

print("Test")
tabX1 = [0, 1, 2, 3]
tabY1 = [1, 2, 3, 4]
tabX2 = [0, 1, 2]
tabY2 = [5, 6, 7]

x, y = Splot.SplotDyskretny(tabX1, tabY1, tabX2, tabY2)
print(x)
print(y)

tabx = []
taby = []

for x in range(25):
    tabx.append(x)
    taby.append(OknoHanninga.hanning(x, 25))

DrawPlot.normalPlot(tabx, taby)
