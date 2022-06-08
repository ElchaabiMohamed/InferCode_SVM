def moyenne(liste):
  if len(liste)==0:
    res=None
    return res
 
  else:
    s=0
    for elem in liste:
      s+=elem
    res=s//len(liste)
  return res