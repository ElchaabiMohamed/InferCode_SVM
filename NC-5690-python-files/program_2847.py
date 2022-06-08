def nextConway(s):
    cpt = 0
    valeur = s[0]
    res = ""
    for elem in s:
        if elem == valeur:
            cpt = cpt + 1
        else:
            res = res + str(cpt) + str(valeur)
            cpt = 1
            valeur = elem
    res = res + str(cpt) + str(valeur)
    return res