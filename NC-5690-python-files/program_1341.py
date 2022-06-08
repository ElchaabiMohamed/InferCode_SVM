def verifSuiteAriGeo(liste,a,b):
    if liste==[]:
      ok=True
    else:
      ok=True
      i=1
      while i<len(liste) and ok:
        if a*liste[i-1]+b!=liste[i]:
          ok=False
        i+=1
    return ok