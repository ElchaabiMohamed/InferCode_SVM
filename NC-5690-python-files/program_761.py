def maximum(liste):
  if liste==0:
    res=None
  else:
    res=0
    for i in range (len,liste):
      if liste[i]>res:
        res=liste[i]
  return res