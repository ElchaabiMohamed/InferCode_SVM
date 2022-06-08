def suiteAriGeo(liste):
  ok=True
  i=0
  j=0
  R=0
  if len(liste)<=2 :
    ok=True
  else :
    for elem in (liste) :
      if liste[0]==0 :
        Q=1
      else :
        Q=(liste[1]/liste[0])
        R=(liste[1]-liste[0])
    while j<(len(liste)-1) :
      if liste[j+1]==liste[j]+R :
        Q=1
      elif liste[j+1]==Q*liste[j] :
        R=0
      j+=1
      
    while i<(len(liste)-1) and ok :
      if liste[i+1]!=Q*liste[i]+R :
        ok=False
      i+=1
  return ok