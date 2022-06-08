def ecart(liste):
  if len(liste)==0:
    res=None
  else:
    res=0
    max=0
    min=0
    for i in range(len(liste)):
      if liste[i]<res:
        min=liste[i]
      if liste[i]>res:
        max=liste[i]
        res=max-min
    return res