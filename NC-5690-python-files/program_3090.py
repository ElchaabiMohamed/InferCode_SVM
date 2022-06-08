def nbOccurrencesLettre(lettre,mot):
  if mot=='':
    res=None
  for i in range(mot):
    if mot[i]==lettre:
      res=res+1
  return res