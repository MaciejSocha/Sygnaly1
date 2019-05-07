def MaximumDif(xTabOrg, yTabOrg, xTabPor, yTabPor):
    max_dif = 0
    size_org = len(xTabOrg)
    size_por = len(xTabPor)

    lim = min(size_org, size_por)
    iterator = 0
    while iterator < lim:
        abs_dif = abs(yTabOrg[iterator]-yTabPor[iterator])
        if max_dif < abs_dif:
            max_dif = abs_dif
        iterator += 1
    return max_dif
