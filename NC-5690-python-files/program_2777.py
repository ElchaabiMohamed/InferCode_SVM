def suiteGeo(liste):
  i=0
  c=True
  if len(liste)==0:
    c=True
  elif 0 in liste:
    c=False
  else:
    a=liste[1]/liste[0]
    while i<(len(liste)-1) and c:
      if liste[i+1]/liste[i]!=a:
        c=False
      i=i+1
  return c