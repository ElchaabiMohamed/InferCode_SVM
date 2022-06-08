def minimum(liste):
  if len(liste)==0:
    res=None
  else:
    for elem in liste:
      if elem<liste[0]:
        res=liste[0]
  return res