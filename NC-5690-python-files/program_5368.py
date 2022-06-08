def minimum(liste):
  if liste==[]:
    res=None
  else:
    res=liste[0]
    for i in range(1,len(liste)-1):
      if liste[i]<liste[i+1]:
        res=liste[i]
  return res