def verifSuiteAriGeo(liste,a,b):
  ok=True
  i=0
  if len(liste)<=1 :
    ok=True
  else :
    while i<(len(liste)-1) and ok :
      if (a*liste[i]+b)!=liste[i+1] :
        ok=False
  return ok