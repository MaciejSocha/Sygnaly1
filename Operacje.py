def suma(xTab1, yTab1, xTab2, yTab2):
    if len(xTab1) < len(xTab2):
        mx = len(xTab1)
    else:
        mx = len(xTab2)
    i = 0
    xTabRes = []
    yTabRes = []
    while i < mx:
        xTabRes.append(xTab1[i])
        yTabRes.append(yTab1[i] + yTab2[i])
        i += 1
    return xTabRes, yTabRes


def roznica(xTab1, yTab1, xTab2, yTab2):
    if len(xTab1) < len(xTab2):
        mx = len(xTab1)
    else:
        mx = len(xTab2)
    i = 0
    xTabRes = []
    yTabRes = []
    while i < mx:
        xTabRes.append(xTab1[i])
        yTabRes.append(yTab1[i] - yTab2[i])
        i += 1
    return xTabRes, yTabRes


def iloczyn(xTab1, yTab1, xTab2, yTab2):
    if len(xTab1) < len(xTab2):
        mx = len(xTab1)
    else:
        mx = len(xTab2)
    i = 0
    xTabRes = []
    yTabRes = []
    while i < mx:
        xTabRes.append(xTab1[i])
        yTabRes.append(yTab1[i] * yTab2[i])
        i += 1
    return xTabRes, yTabRes


def iloraz(xTab1, yTab1, xTab2, yTab2):
    if len(xTab1) < len(xTab2):
        mx = len(xTab1)
    else:
        mx = len(xTab2)
    i = 0
    xTabRes = []
    yTabRes = []
    while i < mx:
        xTabRes.append(xTab1[i])
        if yTab2[i] != 0:
            yTabRes.append(yTab1[i] / yTab2[i])
        else:
            yTabRes.append(0)
        i += 1
    return xTabRes, yTabRes


def nextPowerOf2(n):
    count = 0;

    # First n in the below
    # condition is for the
    # case where n is 0
    if (n and not (n & (n - 1))):
        return n

    while (n != 0):
        n >>= 1
        count += 1

    return 1 << count;
