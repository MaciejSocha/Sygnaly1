import matplotlib.pyplot as plt
import SygnalyCiagle

# plt.plot([1, 2, 3, 4])
# plt.show()

print("Hello")
# inp = input("Enter:")
# print(inp)

sig = SygnalyCiagle.SinusoidalnyWyprostowanyDwupolowkowo(1, 20, 0.0, 20)

sig2 = SygnalyCiagle.SinusoidalnyWyprostowanyDwupolowkowo(0.5, 5, 0.0, 20)

xTab = []
yTab = []
x = 0
yTab2 = []

while x < 50:
    xTab.append(x)
    yTab.append(sig.x(x))
    yTab2.append(sig2.x(x))
    x += 0.1

plt.plot(xTab, yTab)
plt.plot(xTab, yTab2)
plt.show()
