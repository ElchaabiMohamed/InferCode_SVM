def verifSuiteAriGeo(liste,a,b):
  ok=True
  i=0
  while i<len(liste)-1 and ok:
    if liste[i]!=a*liste[i+1]+b:
      ok=False
    i+=1
  return ok