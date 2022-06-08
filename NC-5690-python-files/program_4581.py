def maximum(liste):
  if len(liste)==0:
     res=None
  else:
    res=None
    for i in range(len(liste)):
      if liste[i]>res:
        res=liste[i]
  return res