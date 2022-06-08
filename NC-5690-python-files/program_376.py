def maximum(liste):
  if len(liste)==0:
    res=None
  else:
    res=[]
    for i in range(len(liste)):
      if len(liste+1)>len(liste):
        res=len(liste+1)
  return res