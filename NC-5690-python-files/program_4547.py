def verifSuiteAriGeo(liste,a,b):
  ok=True
  i=0
  if len(liste)==0 or len(liste)==1:
    ok=True
  while i<len(liste)!=liste[0] and ok:
    if liste[i]!=a*liste[i-1]+b:
      ok=False
    i=i+1
  return ok