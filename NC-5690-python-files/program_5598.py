def suiteGeo(liste):
  i=0
  ok=True
  if 0 in liste:
    ok=False
  elif len(liste)>1:
    raison=liste[-1]/liste[-2]
    while i<len(liste)-1:
      if liste[i+1]!=liste[i]*raison:
        ok=False
      i+=1
  return ok