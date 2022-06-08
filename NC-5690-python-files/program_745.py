def sommeNbPairs(liste):
  res=0
  for i in range(len(liste)):
    if len(liste)%2!=0:
      res=res+liste[i]
  return res