def ecart(liste):
  if len(liste)==0:
    res=None
  else:
    min=liste[0]
    max=liste[0]
    res=0
    for i in range(1,len(liste)):
      if min>liste[i]:
        min=liste[i]
      if max<liste[i]:
        max=liste[i]
      res=max-min
    return res