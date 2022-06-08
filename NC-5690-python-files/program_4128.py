def nextConway(s):
    cpt = 0
    valeur = s[0]
    res = ""
    for num in s:
        if num == valeur:
            cpt = cpt + 1
        else:
            res = res + str(cpt) + str(valeur)
            cpt = 1
            valeur = num
    res = res + str(cpt) + str(valeur)
    return res