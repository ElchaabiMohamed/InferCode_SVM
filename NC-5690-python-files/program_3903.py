def suiteAri(liste):
  res=True
  if len(liste)>1:
    r=liste[1]-liste[0]
    res=True
    n=1
    while n<len(liste) and ok:
      if liste[n]!=liste[n-1]*1+r:
        ok=False
      n+=1
  return res