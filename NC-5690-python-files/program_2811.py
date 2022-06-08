def maximum(liste):
  res=max
  for i in range (len(liste)):
    res=i<res
  return res