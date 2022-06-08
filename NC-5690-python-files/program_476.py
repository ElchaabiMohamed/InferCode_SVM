def maximum(liste):
  res=0
  for i in range(len(liste)) :
    if liste[i]>0 :
      res=res+liste[i]
    else :
      res=None
  return res