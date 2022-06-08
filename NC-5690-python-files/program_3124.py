def suiteGeo(liste):
    if liste==[] or len(liste)==1:
      ok=True
    elif 0 in liste:
      ok=False
    else:
      ok=True
      i=0
      while i<len(liste)+1 and ok:
        cte=liste[i+1]/liste[i]
        if liste[0]*cte**i!=liste[i+1]:
          ok=False
        i+=1
    return ok