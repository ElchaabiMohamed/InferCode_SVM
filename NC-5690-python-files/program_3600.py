def minimum(liste):
  if len(liste)==0:
    res=None
  else:
    res=liste[0]
    for i in range(1,len(liste)-1):
      if liste[i]<res:
        res=liste[i]
  return res