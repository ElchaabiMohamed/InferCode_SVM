def minimum(liste):
  if len(liste)==0:
    res=None
  else:
    res=liste[0]
    for elem in liste:
      if elem<liste[elem]:
        res=liste[elem]
  return res