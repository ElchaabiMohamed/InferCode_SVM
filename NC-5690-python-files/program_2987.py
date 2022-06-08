def ecart(liste):
  res=0
  x=0
  y=0
  if len(liste)==0:
    res=None
  if len(liste)==1:
    res=0
  else:
    x=liste[0]
    y=x
    for i in range(len(liste)):
      if liste[i]>x:
        x=liste[i]
      else:
        y=liste[i]
    res=x-y
    return res