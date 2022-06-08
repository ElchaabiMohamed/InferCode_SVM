def maximum(liste):
  res=liste[0]
  for i in range (len(liste)):
    res=res<i
  return res