from scipy.linalg import hadamard

print(hadamard(256))


def calc(tabX, tab):
    pow2 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
    w = 0
    nb = tab.__len__()
    print(nb)
    if nb in pow2:
        hd = hadamard(nb)
    else:
        i = 0
        while i < 13:
            if pow2[i] < nb < pow2[i + 1]:
                w = pow2[i + 1]
            i += 1
    print(w)
    diff = w - nb
    print(tabX)
    it = tabX.__len__()
    itt = tabX[it-1]
    for x in range(diff):
        itt += 0.0625
        tab.append(0)
        tabX.append(itt)

    # Main part
    hd = hadamard(w)
    newtab = [[0 for x in range(w)] for y in range(1)]
    for x in range(nb-1):
        newtab[0][x] = tab[x]
    tabret = hd * newtab
    return tabX, tabret
