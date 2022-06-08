def moyenne(liste):
  if len(liste)==0:
    res=None
  else:
    for elem in liste:
      s+=elem
    res=s//len(liste)
  return res