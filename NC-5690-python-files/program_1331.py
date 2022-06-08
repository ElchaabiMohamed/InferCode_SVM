def moyenne(liste):
  res=0
  compteur=0
  for element in liste:
    res=res+element
    compteur=compteur+1
  if compteur==0:
    res=None
  else:
    res=res/compteur
  return res