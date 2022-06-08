def maximum(liste):
  if len(liste)==0:
    res=None
  else:
    res=[]
    for i in range(len(liste)):
      if liste[1+i]>liste[i]:
        res=liste[1+i]
  return res