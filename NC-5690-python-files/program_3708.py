def suiteGeo(liste):
  ok=True
  i=0
  if len(liste)<=1 :
    ok=True
  else :
    while i<(len(liste)-1) and ok :
      if liste[0]==0 :
        ok=False
      elif liste[i]!=(liste[0]*(liste[i+1]//liste[i])**i):
        ok=False
      i+=1
  return ok