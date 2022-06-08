def somme(liste):
  if len(liste)==0:
    return 0
  res=0
  for elem in liste:
    res=res+elem
  return res