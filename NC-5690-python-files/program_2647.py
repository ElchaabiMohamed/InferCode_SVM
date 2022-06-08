def moyenne(liste):
  res=0
  cpt=0
  for elem in liste:
    res=res+elem
    cpt=cpt+1
  if cpt==0:
    res=None
  else:
    res=res/cpt
  return res 