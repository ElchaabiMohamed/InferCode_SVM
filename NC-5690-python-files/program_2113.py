def suiteAriGeo(liste):
  ok=True
  i=0
  R=0
  Q=0
  if len(liste)<=2 :
    ok=True
  else :
    for elem in (liste) :
      if liste[0]==0 :
        Q=1
      elif (liste[i+1]-liste[i])==(liste[i+2]-liste[i+1]) :
        Q=1
        R=(liste[1]-liste[0])
      elif (liste[i+1]/liste[i])==(liste[i+2]/liste[i+1]) :
        Q=(liste[1]/liste[0])
        R=0
      
    while i<(len(liste)-1) and ok :
      if liste[i+1]!=Q*liste[i]+R :
        ok=False
      i+=1
  return ok