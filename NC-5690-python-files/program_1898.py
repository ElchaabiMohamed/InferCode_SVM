def suiteGeo(liste):
  ok=True
  i=0
  if len(liste)<=1 :
    ok=True
  else :
    while i<(len(liste)-1) and ok :
      if liste[0]==0 :
        Q=0
      else :
        Q=(liste[i+1]/liste[i])
      if liste[i+1]!=(Q*liste[i]):
        ok=False
      i+=1
  return ok