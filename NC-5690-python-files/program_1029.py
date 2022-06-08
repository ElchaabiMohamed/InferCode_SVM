def ecart(liste):
  res1=liste[0]
  res2=liste[0]
  for i in range(1,len(liste)):
    if liste[i]>res1:
      res1=liste[i]
    if liste[i]<res2:
      res2=liste[i]
  res=res1-res2
  return res