def suiteGeo(liste):
  ok=True
  i=0
  if len(liste)<=1 :
    ok=True
  else :
    if liste[0]==0 :
      Q=0
    else :
      Q=(liste[1]/liste[0])
    while i<(len(liste)-1) and ok :
      if liste[i+1]!=(Q*liste[i]):
        ok=False
      i+=1
  return ok 