import DrawPlot
import SygnalyCiagle
from Part4 import Sinus, WalshHadamard, FastWalshHadamard

xTab = []
yTab = []
x = 0

while x < 6:
    xTab.append(x)
    yTab.append(Sinus.multisinus(x))
    x += 0.01

# DrawPlot.normalPlot(xTab, yTab)

xx, yy = Sinus.rangesinus(0, 6)
# xx, yy = SygnalyCiagle.Sinusoidalny(1, 3, 0, 10, 0.1).mkTab()

# DrawPlot.normalPlot(xx, yy)

whxx, whyy = WalshHadamard.calc(xx, yy)

DrawPlot.normalPlot(whxx, whyy)

why = FastWalshHadamard.fwht(yy)

DrawPlot.normalPlot(whxx, why)
