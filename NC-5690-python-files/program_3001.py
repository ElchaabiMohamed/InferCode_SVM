def suiteGeo(liste):
  i=0
  ok=True
  if len(liste)>1 and 0 in liste:
    ok=False
  elif len(liste)>1:
    while i>-len(liste):
      if liste[-i-1]/liste[-i-2]!=liste[-i-3]/liste[-i-2]:
        ok=False
      i+=1
  return ok