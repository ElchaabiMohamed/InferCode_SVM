def suiteGeo(liste):
    res = True
    if len(liste)>1:
        if  liste[0] == 0:
            q = 0
        else:
            q = liste[1]/liste[0]    
        res=verifSuiteAriGeo(liste,q,0)

    return res
  
  
  
  
def verifSuiteAriGeo(liste,a,b):
    res=True
    n=1
    while n<len(liste) and res:
        if liste[n]!=liste[n-1]*a+b:
            res=False
        n+=1
    return res