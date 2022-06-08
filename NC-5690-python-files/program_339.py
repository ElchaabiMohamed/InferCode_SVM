def ecart(liste):
  res=0
  if len(liste)==0:
    res=None
  if len(liste)==1:
    res=0
  x=liste[0]
  y=liste[0]
  for i in range(1,len(liste)):
    if liste[i]>x:
      x=liste[i]
    if liste[i]<y:
      y=liste[i]
  res=x-y
  return res