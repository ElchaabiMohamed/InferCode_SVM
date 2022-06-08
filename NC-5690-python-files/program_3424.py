def suiteGeo(liste):
    if liste==[] or len(liste)==1:
      ok=True
    elif 0 in liste:
      if liste[0]!=0:
        ok=True
      else:
        while 0 in liste:
          liste.remove(0)
        if liste==[]:
          ok=True
        else:
          ok=False
    else:
      ok=True
      i=1
      while i<len(liste) and ok:
        cte=liste[i]/liste[i-1]
        if liste[0]*cte**i!=liste[i]:
          ok=False
        i+=1
    return ok