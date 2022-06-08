def maximum(liste):
  if len(liste)==0:
    res=None
  res=[]
  for i in range(len(liste)):
    if liste[i]+1>liste[i]:
      res=liste[i]+1
  return res