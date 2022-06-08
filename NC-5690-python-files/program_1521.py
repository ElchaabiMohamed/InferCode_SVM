def suiteGeo(liste):
    if len(liste) == 0 or len(liste) == 1:
        res = True
    else:
        test = liste[1]/liste[0]
        if len(liste) >= 3:
            for i in range(2,len(liste)):
                if liste[i]/liste[i-1] == test:
                    res = True
                else:
                    res = False
        else:
            res = True
    return res