def maximum(liste):
  res=l[0]
  for i in range(0,len(liste)):
    if res<i:
      res=i
  return res