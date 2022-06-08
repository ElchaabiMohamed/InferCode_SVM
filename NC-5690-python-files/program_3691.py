def suiteGeo(liste):
  i=-1
  ok=True
  if 0 in liste:
    ok=False
  elif len(liste)>1:
    raison=liste[-1]/liste[-2]
    while i>-len(liste):
      if liste[i-1]!=0 and liste[i]%liste[i-1]!=0:
        ok=False
      i-=1
  return ok