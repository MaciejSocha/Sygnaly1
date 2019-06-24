import DrawPlot
from Part4 import Sinus

xTab = []
yTab = []
x = 0

while x < 6:
    xTab.append(x)
    yTab.append(Sinus.multisinus(x))
    x += 0.01

DrawPlot.normalPlot(xTab, yTab)

xx, yy = Sinus.rangesinus(0, 6)

DrawPlot.normalPlot(xx, yy)
