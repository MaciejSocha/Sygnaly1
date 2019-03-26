import matplotlib.pyplot as plt
import SygnalyCiagle
import Szumy
import SygnalyDyskretne

# plt.plot([1, 2, 3, 4])
# plt.show()

print("Hello")
# inp = input("Enter:")
# print(inp)

sig = SygnalyCiagle.Trojkatny(5, 5, 0, 0, 0.5)
# sig = SygnalyDyskretne.SzumImpulsowy(5, 0, 0, 0, 0.2)
xTab = []
yTab = []
x = 0
maks = 0
tmp = 0

while x < 50:
    xTab.append(x)
    tmp = sig.x(x)
    yTab.append(tmp)
    if maks < tmp:
        maks = tmp
    x += 0.1

plt.plot(xTab, yTab)

print(maks)
# plt.axis([-0.2, 20.2, -1.2, 1.2])
plt.show()
