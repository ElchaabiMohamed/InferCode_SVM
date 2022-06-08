def ecart(liste):
  if liste==[]:
    res=None
  else:
    if len(liste)==1:
      res=0
    else:
      max=liste[0]
      min=liste[0]
      for i in range(len(liste)):
        if liste[i]>max:
          max=liste[i]
      for i in range(len(liste)):
        if liste[i]<min:
          min=liste[i]
      res=max-min
  return res