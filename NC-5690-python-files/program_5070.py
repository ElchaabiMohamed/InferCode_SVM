def ecart(liste):
  if len(liste)==0:
    res=None
  else:
    max=0
    min=0
    for i in range(len(liste)):
      if liste[i]>max:
        max=liste[i]
    for i in range(len(liste)):
      if liste[i]<min:
        min=liste[i]
    res=max-min
    return res