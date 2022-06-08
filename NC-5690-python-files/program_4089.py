def minimum(liste):
  if liste==[]:
    min=None
  else:
    min=liste[0]
    for i in range(len(liste)):
      if liste[i]<min:
        min=liste[i]
  return min