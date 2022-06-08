def maximum(liste):
  if len(liste)==0:
    res=None
  else:
    for i in range(len(liste)):
      if liste[i]>i:
        res=liste[i]
  return res