def suiteAriGeo(liste):
    if liste==[] or len(liste)==1:
      ok1=True
    else:
      ok1=True
      ctePrec=liste[1]-liste[0]
      cteAct=None
      i=2
      while i<len(liste) and ok1:
        cteAct=liste[i]-liste[i-1]
        if cteAct!=ctePrec:
          ok1=False
        ctePrec=cteAct
        i+=1
    if liste==[] or len(liste)==1:
      ok2=True
    elif 0 in liste:
      if liste[0]!=0:
        ok2=True
      while 0 in liste:
        liste.remove(0)
      if liste==[]:
        ok2=True
      else:
        ok2=False
    else:
      ok2=True
      i=1
      while i<len(liste) and ok2:
        cte=liste[i]/liste[i-1]
        if liste[0]*cte**i!=liste[i]:
          ok=False
        i+=1
    return ok1 or ok2