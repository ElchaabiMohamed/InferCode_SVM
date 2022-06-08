def verifSuiteAriGeo(liste,a,b):
  ok=True
  i=0
  if len(liste)<=1 :
    ok=True
  else :
    while i<len(liste) and ok :
      if liste[i+1]!=a*liste[i]+b :
        ok=False
      i+=1
  return ok