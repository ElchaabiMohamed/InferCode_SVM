def sommeNbPairs(liste):
  for i in range(len(liste)):
    if [i]%2==0:
      res=res+[i]
  return res