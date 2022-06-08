def verifSuiteAriGeo(liste,a,b):
    if liste == [] or len(liste) == 1:
        res = True
    flag = True
    i = 0
    while flag == True and i < len(liste)-1:
        if liste[i+1] == (a * liste[i]) + b:
            flag = True
        else:
            flag = False
        i += 1
    res = flag
    return res