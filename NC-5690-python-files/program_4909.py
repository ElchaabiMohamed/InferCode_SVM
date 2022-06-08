def maximum(liste):
  if len(liste)==0:
    res=None
  else:
    for i in range(liste):
      if liste[i]>res:
        res=liste[i]
  return res