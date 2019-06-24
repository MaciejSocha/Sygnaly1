import math

def DFT(xTab,yTab):
    YTab = []
    YiTab = []
    N = len(xTab)
    for m in range(0,N):
        sum = 0
        sumi = 0
        for n in range(0,N):
            x, xi = Euler(m,n,N)
            sum += yTab[n]*x
            sumi += yTab[n]*xi
        YTab.append(sum)
        YiTab.append(sumi)
    return xTab, YTab, YiTab


def Euler(m, n, N):
    x = math.sin(-((2*math.pi*m)/N)*n)
    xi = math.cos(-((2*math.pi*m)/N)*n)
    return x, xi

