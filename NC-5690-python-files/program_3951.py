def verifSuiteAriGeo(liste,a,b):
    res=True
    n=1
    while n<len(liste) and res:
        if liste[n]!=liste[n-1]*a+b:
            res=False
        n+=1
    return res


def suiteAriGeo(liste):
  res = True
  if len(liste) > 2:
    if liste[1]-liste[0] == 0:
        q = 0
    else:
        q = (liste[2]-liste[1])/(liste[1]-liste[0])
        
    r = liste[1] - (q*liste[0])
    res=verifSuiteAriGeo(liste,q,r)
    
  return res