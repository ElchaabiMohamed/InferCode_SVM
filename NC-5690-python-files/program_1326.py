def suiteAri(liste):
    if liste==[]:
      ok=True
    else:
      ok=True
      ctePrec=liste[1]-liste[0]
      cteAct=None
      i=2
      while i<len(liste) and ok:
        cteAct=liste[i]-liste[i-1]
        if cteAct!=ctePrec:
          ok=False
        ctePrec=cteAct
    return ok