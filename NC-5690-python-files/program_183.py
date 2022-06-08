def maximum(liste):
  if liste==[]:
    return None
  else :
    res=liste[0]
    for i in range(1,len(liste)):
      if res<liste[i]:
        res=liste[i]
  return res