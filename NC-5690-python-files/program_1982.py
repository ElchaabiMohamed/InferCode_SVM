def verifSuiteAriGeo(liste,a,b):
  ok=True
  i=0
  while i<len(liste) and ok:
    ok=liste[i]==a*liste[i+1]+b 
    prec=ok
    i+=1
  return ok