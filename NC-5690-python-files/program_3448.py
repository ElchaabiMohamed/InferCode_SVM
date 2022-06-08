def moyenne(liste):
  if liste==[]:
    res=None
  else:
    res=0
    for elem in liste:
      res+=elem
    res=res/len(liste)
  return res