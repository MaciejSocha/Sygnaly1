import math

def DFT(xTab,yTab,M):
    YTab = []
    YiTab = []
    XTab = []
    YmodTab = []
    N = len(xTab)
    for m in range(0,M):
        sum = 0
        sumi = 0
        for n in range(0,N):
            x, xi = Euler(m,n,N)
            sum += yTab[n]*x
            sumi += yTab[n]*(-xi)
        sum /= N
        sumi /= N
        YTab.append(sum)
        YiTab.append(sumi)
        XTab.append(m)
        YmodTab.append(math.sqrt(pow(sum,2)+pow(sumi,2)))
    return XTab, YTab, YiTab, YmodTab


def Euler(m, n, N):
    x = math.cos(((2*math.pi*m*n)/N))
    xi = math.sin(((2*math.pi*m*n)/N))
    return x, xi

def FFT():

    return 1
