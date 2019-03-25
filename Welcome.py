import matplotlib.pyplot as plt
import SygnalyCiagle

# plt.plot([1, 2, 3, 4])
# plt.show()

print("Hello")
# inp = input("Enter:")
# print(inp)

sig = SygnalyCiagle.Sinusoidalny(1, 10, 0, 0)

xTab = []
yTab = []
x = 0

while x < 20:
    xTab.append(x)
    yTab.append(sig.x(x))
    x += 0.1

plt.plot(xTab, yTab)
# plt.axis([-0.2, 20.2, -1.2, 1.2])
plt.show()
