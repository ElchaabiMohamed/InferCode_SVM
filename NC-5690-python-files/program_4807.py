def minimum(liste):
  if len(liste)==0:
    res=None
  else:
    res=liste[0]
    for i in liste[i]:
      if liste[i]<res:
        res=liste[i]
  return res