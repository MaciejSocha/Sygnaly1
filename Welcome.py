import matplotlib.pyplot as plt
import SygnalyCiagle
import Szumy
import SygnalyDyskretne
import DrawPlot as plot

# plt.plot([1, 2, 3, 4])
# plt.show()

print("Hello")
# inp = input("Enter:")
# print(inp)

sig = SygnalyCiagle.Sinusoidalny(1, 10, 0, 0)
# sig = Szumy.SzumGausa(5, 0, 0)
xTab = []
yTab = []
x = 0
tmp = 0

while x < 50:
    xTab.append(x)
    # tmp = sig.x(x)
    yTab.append(sig.x(x))
    x += 0.1

# plt.plot(xTab, yTab)

plot.normalPlot(xTab, yTab)
plot.histPlot(yTab, 10)
# plt.axis([-0.2, 20.2, -1.2, 1.2])
# plt.show()
