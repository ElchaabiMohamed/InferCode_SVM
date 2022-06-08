def nbOccurrencesLettre(lettre,mot):
  res=0
  for i in range(len(mot)):
    if lettre==mot[i]:
      res=res+1
  return res