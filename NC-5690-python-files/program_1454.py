def suiteAri(liste):
  ok=True
  i=0
  if len(liste)==0:
    ok=True
  while i<len(liste)-1 and ok:
    if liste[i+1]!=liste[i]+liste[i+1]-liste[i]:
      ok=False
    i=i+1
  return ok