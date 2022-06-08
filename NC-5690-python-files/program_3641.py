def suiteGeo(liste):
  i=0
  c=True
  if len(liste)==0:
    c=True
  elif 0 in liste:
    c=False
  else:
    while i<(len(liste)-2) and c:
      if liste[i+2]/liste[i+1]!=liste[i+1]/liste[i]:
        c=False
      i=i+1
  return c