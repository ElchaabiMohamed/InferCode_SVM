def suiteAri(liste):
  ok=True
  i=0
  while i<len(liste)-1 and ok:
    r=liste[1]-liste[0]
    if liste[i+1]-liste[i]!=r:
      ok=False
    i=i+1
  return ok