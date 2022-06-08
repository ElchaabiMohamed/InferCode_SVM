def minimum(liste):
  if liste==[]:
    res=None
  else:
    res=liste[0]
    for i in range(1,len(liste)):
      if liste[i]>liste[i+1]:
        res=liste[i]
  return res