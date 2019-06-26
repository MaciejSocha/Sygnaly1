import DrawPlot
import SygnalyCiagle
from Part4 import Sinus, WalshHadamard, FastWalshHadamard
import timeit

start = timeit.default_timer()
# xTab = []
# yTab = []
# x = 0

# while x < 6:
    # xTab.append(x)
    # yTab.append(Sinus.multisinus(x))
    # x += 0.01

# DrawPlot.normalPlot(xTab, yTab)

xx, yy = Sinus.rangesinus(0, 10)
# xx, yy = SygnalyCiagle.Sinusoidalny(1, 1, 0, 10, 1/50).mkTab()
# xx, yy = SygnalyCiagle.Prostokatny(1, 2, 0, 10, 0.5, 1/50).mkTab()

# DrawPlot.normalPlot(xx, yy)

whxx, whyy = WalshHadamard.calc(xx, yy)

# DrawPlot.normalPlot(whxx, whyy)

# whx, why = FastWalshHadamard.fast(xx, yy)

# DrawPlot.normalPlot(whx, why)

stop = timeit.default_timer()
print('Time: ', stop - start)
