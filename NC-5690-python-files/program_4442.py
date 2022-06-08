def verifSuiteAriGeo(liste,a,b):
    liste2 = [liste[0]] + [liste[nb-1]*a+b for nb in range(1,len(liste))]    
    return liste == liste2