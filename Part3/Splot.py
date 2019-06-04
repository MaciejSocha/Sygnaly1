
def SplotDyskretny(tabX1,tabY1,tabX2,tabY2):
    xTab = []
    yTab = []
    if len(tabX1) == len(tabX2):
        i = 0
        for val in reversed(tabY2):
            xTab[i] = tabX1
            yTab[i] = tabY1[i]+val
    return xTab, yTab

