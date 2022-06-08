def suiteGeo(liste):
  i=-1
  ok=True
  if len(liste)>1:
    while i>-len(liste):
      if liste[i-1]!=0 and liste[i]%liste[i-1]!=0:
        ok=False
      i-=1
  if 0 in liste:
    ok=False
  return ok