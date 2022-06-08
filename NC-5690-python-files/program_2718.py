def suiteGeo(liste):
    if liste==[] or len(liste)==1:
      ok=True
    elif 0 in liste:
      ok=False
    else:
      ok=True
      i=1
      while i<len(liste)+1 and ok:
        cte=liste[i]/liste[i-1]
        if liste[0]*cte**i!=liste[i+1]:
          ok=False
        ctePrec=cteAct
        i+=1
    return ok