import matplotlib.pyplot as plt
import SygnalyCiagle

# plt.plot([1, 2, 3, 4])
# plt.show()

print("Hello")
# inp = input("Enter:")
# print(inp)

sig = SygnalyCiagle.SinusoidalnyWyprostowanyDwupolowkowo(1, 20, 0.0, 20)

xTab = []
yTab = []
x = 0

while x < 50:
    xTab.append(x)
    yTab.append(sig.x(x))
    x += 0.1

plt.plot(xTab, yTab)
plt.show()
