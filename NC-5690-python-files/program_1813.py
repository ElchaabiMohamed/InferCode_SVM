def verifSuiteAriGeo(liste,a,b):
    res = True
    if len(liste) < 0:
        liste2 = [liste[0]] + [liste[nb-1]*a+b for nb in range(1,len(liste))]    
        res = liste == liste2
    return res