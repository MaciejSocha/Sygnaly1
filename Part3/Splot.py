
def SplotDyskretny(tabX1, tabY1, tabX2, tabY2):
    yTab = []
    xTab = []
    i = 0
    M = len(tabY1)
    N = len(tabY2)
    if tabX1[1] != tabX2[1]:
        print("UWAGA SPRAWDŹ OKRESY SYGNAŁÓW")
    for x in range(M + N - 1):
        sum = 0
        j = 0
        for val in tabY1:
            if i-j < len(tabY2) and i-j >= 0:
                sum += val*tabY2[i-j]
            j += 1
        xTab.append(i * tabX1[1])
        yTab.append(sum)
        i += 1

    return xTab, yTab

