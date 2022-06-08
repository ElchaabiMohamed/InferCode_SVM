def suiteAriGeo(liste):
  ok=True
  i=0
  if len(liste)<=1 :
    ok=True
  else :
    for elem in (liste) :
      if liste[0]==0 :
        Q=0
      else :
        Q=(liste[1]/liste[0])
        R=(liste[1]-liste[0])
    while i<(len(liste)-1) and ok :
      if liste[i+1]!=Q*liste[i]+R :
        ok=False
      i+=1
  return ok