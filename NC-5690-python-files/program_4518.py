def suiteGeo(liste):
  ok=True
  i=0
  if len(liste)<=1 :
    ok=True
  else :
    while i<(len(liste)-1) and ok :
      if (liste[i]*liste[i+1])==0 :
        ok=False
      elif liste[i]!=(liste[0]*(liste[0]//liste[1])**i):
        ok=False
      i+=1
  return ok