import matplotlib.pyplot as plt
import SygnalyCiagle
import Szumy
import SygnalyDyskretne
import DrawPlot as plot
import Operacje

# plt.plot([1, 2, 3, 4])
# plt.show()

print("Hello")
# inp = input("Enter:")
# print(inp)

# sig = SygnalyCiagle.Trojkatny(1, 10, 0, 50, 0.3, 0.1)
# sig = Szumy.SzumGausa(5, 0, 20, 0.05)
# sig = SygnalyDyskretne.SzumImpulsowy(1, 0, 50, 1, 0.5)
sig = SygnalyCiagle.Sinusoidalny(1, 15, 0, 30, 0.2)
sig2 = SygnalyCiagle.Prostokatny(1, 15, 0, 30, 0.5, 0.2)
x = 0
tmp = 0

# while x < 50:
# xTab.append(x)
# tmp = sig.x(x)
# yTab.append(sig.x(x))
# x += 0.1


xTab, yTab = sig.mkTab()
xTab2, yTab2 = sig2.mkTab()

# plt.plot(xTab, yTab)

plot.normalPlot(xTab, yTab)
plot.normalPlot(xTab2, yTab2)
# plot.histPlot(yTab, 20)
# plot.discreetPlot(xTab, yTab)
# plt.axis([-0.2, 20.2, -1.2, 1.2])
# plt.show()

# print(sig.mcSr())

xRes, yRes = Operacje.iloczyn(xTab2, yTab2, xTab, yTab)

plot.normalPlot(xRes, yRes)
