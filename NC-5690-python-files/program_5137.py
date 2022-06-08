def moyenne(liste):
  if len(liste)!=0:
    s=0
    for elem in liste:
      s+=elem
    res=s//len(liste)
  else:
    res=None
    
  return res