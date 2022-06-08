def suiteAri(liste):
  ok=True
  i=0
  if len(liste)<=2 :
    ok=True
  else :
    while i<(len(liste)-2) and ok :
      if (liste[i+1]-liste[i])!=(liste[i+2]-liste[i+1]) :
        ok=False
  return ok