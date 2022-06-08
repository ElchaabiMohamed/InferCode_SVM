def verifSuiteAriGeo(liste,a,b):
  ok=True
  i=0
  while i<len(liste) and ok:
    if liste[i]!=a*liste[i-1]+b:
      ok=False
    i=i+1
    if len(liste)==0 or len(liste)==1:
      ok=True
  return ok