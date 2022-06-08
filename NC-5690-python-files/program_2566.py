def nbOccurrencesLettre(lettre,mot):
  if mot=='':
    res=None
  else:
    res=0
    for i in range(len(mot)):
      if mot[i]==lettre:
        res=res+1
  return res
