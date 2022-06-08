def maximum(liste):
  if (liste)==0:
    res=None
  else:
    for i in range(1,len(liste)):
      if liste[i]>res:
        res=res>liste[i]
  return res