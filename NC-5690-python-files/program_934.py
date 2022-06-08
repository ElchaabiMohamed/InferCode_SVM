def maximum(liste):
  if len(liste)==0:
    res=None
  else:
    res=[]
    for i in range(len(liste)):
      res=liste[i]>res
  return res