def save(xTab, yTab, filePath):
    mx = 0
    if len(xTab) != len(yTab):
        if len(xTab) > len(yTab):
            mx = len(xTab)
        else:
            mx = len(yTab)
    else:
        mx = len(xTab)
    i = 0
    f = open(filePath, "w")
    while i < mx:
        f.write(str(xTab[i]))
        f.write(" ")
        f.write(str(yTab[i]))
        f.write("\n")
        i += 1
    f.close()


def load(filePath):
    f = open(filePath, "r")
    xTab = []
    yTab = []
    while f.readable():
        rw_input = f.readline()
        if rw_input is '':
            break
        x, y = rw_input.split()
        xTab.append(float(x))
        yTab.append(float(y))
    f.close()
    return xTab, yTab
