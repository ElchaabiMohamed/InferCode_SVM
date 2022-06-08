def ecart(liste):
  res1=liste[0]
  yres2=liste[0]
  for i in range(1,len(liste)):
    if liste[i]>x:
      x=liste[i]
    if liste[i]<y:
      y=liste[i]
  res=x-y
  return res