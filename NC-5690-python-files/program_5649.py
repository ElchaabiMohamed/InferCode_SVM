def suiteGeo(liste):
  i=1
  ok=True
  if len(liste)>=2:
    raison=liste[1]-liste[0]
    while i<len(liste)-1 and ok:
      ok=liste[i+1]==liste[i]*raison
      i+=1
  return ok