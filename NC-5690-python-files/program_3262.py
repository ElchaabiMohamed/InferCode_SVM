def ecart(liste):
  x=liste[0]
  y=liste[0]
  for i in range(1,len(liste)):
    if liste[i]>x:
      x=liste[i]
    if liste[i]<y:
      y=liste[i]
  res=x-y
  return res