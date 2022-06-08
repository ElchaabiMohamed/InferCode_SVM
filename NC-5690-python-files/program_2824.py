def suiteAri(liste):
    if liste==[]:
      ok1=True
    else:
      ok1=True
      ctePrec=liste[1]-liste[0]
      cteAct=None
      i=2
      while i<len(liste) and ok:
        cteAct=liste[i]-liste[i-1]
        if cteAct!=ctePrec:
          ok1=False
        ctePrec=cteAct
        i+=1
    return ok1

def suiteGeo(liste):
    if liste==[] or len(liste)==1:
      ok2=True
    elif 0 in liste:
      ok2=False
    else:
      ok2=True
      i=1
      while i<len(liste) and ok:
        cte=liste[i]/liste[i-1]
        if liste[0]*cte**i!=liste[i]:
          ok2=False
        i+=1
    return ok2

def suiteAriGeo(liste):
    return ok1 or ok2