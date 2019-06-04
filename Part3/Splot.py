
def SplotDyskretny(tabX1,tabY1,tabX2,tabY2):
    yTab = []
    xTab = []
    i = 0
    M = len(tabY1)
    N = len(tabY2)
    if tabX1 != tabX2:
        print("UWAGA SPRAWDŹ OKRESY SYGNAŁÓW")
    for x in range(M + N - 1):
        sum = 0
        j = 0
        for val in tabY1:
            if i-j < len(tabY2):
                sum += val*tabY2[i-j]
            j += 1
        xTab[i] = i * tabX1
        yTab[i] = sum
        i += 1

    return xTab, yTab

