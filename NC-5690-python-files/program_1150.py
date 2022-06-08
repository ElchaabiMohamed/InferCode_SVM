def suiteGeo(liste):
    if liste==[] or len(liste)==1:
      ok=True
    elif 0 in liste:
      ok=False
    else:
      ok=True
      ctePrec=liste[1]/liste[0]
      cteAct=None
      i=2
      while i<len(liste) and ok:
        cteAct=liste[i]/liste[i-1]
        if cteAct!=ctePrec:
          ok=False
        ctePrec=cteAct
        i+=1
    return ok