import matplotlib.pyplot as plt
import math


def normalPlot(xTab, yTab):
    plt.plot(xTab, yTab)
    plt.grid()
    plt.xlabel("t")
    plt.ylabel("A")
    plt.show()


def histPlot(yTab, parts):
    maxVal = max(yTab)
    minVal = min(yTab)
    szerokosc = ((maxVal - minVal) / (parts - 1))
    mp = {}
    for y in yTab:
        w = math.ceil(y / szerokosc)
        if w not in mp.keys():
            mp[w] = 1
        else:
            mp[w] += 1
    plt.bar(mp.keys(), mp.values())
    plt.show()


def discreetPlot(xTab, yTab):
    plt.plot(xTab, yTab, 'r.')
    plt.grid()
    plt.xlabel("t")
    plt.ylabel("A")
    plt.show()

def FourierMod(xTab, yTab):
    plt.plot(xTab, yTab, 'r.')
    plt.grid()
    plt.title("Moduł FFT")
    plt.xlabel("f[Hz]")
    plt.show()


def complexPlot(xTab, yTab,yiTab):
    plt.subplot(2,1,1)
    plt.plot(xTab, yTab, 'r.')
    plt.grid()
    plt.title("wykres amplitudy od częstotliwości(część rzeczywista)")
    plt.xlabel("f")
    plt.ylabel("A")
    plt.subplot(2,1,2)
    plt.plot(xTab, yiTab, 'r.')
    plt.grid()
    plt.title("wykres amplitudy od częstotliwości(część urojona)")
    plt.xlabel("f")
    plt.ylabel("A")
    plt.show()


def FourierComplexPlot(xTab, yTab,yiTab):
    plt.subplot(2,1,1)
    plt.plot(xTab, yTab, 'r.')
    plt.grid()
    plt.title("Wartości FFT (część rzeczywista)")
    plt.xlabel("f[Hz]")
    plt.subplot(2,1,2)
    plt.plot(xTab, yiTab, 'r.')
    plt.grid()
    plt.title("Wartości FFT (część urojona)")
    plt.xlabel("f[Hz]")
    plt.show()