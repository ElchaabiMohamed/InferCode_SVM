def maximum(liste):
  res=''
  for i in range(len(liste)):
    if res<liste[i]:
      res=liste[i]
  return res