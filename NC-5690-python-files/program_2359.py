def nbOccurrencesLettre(lettre,mot):
  if len(mot)==0:
    res=0
  if len(lettre)==1:
    res=0
  for i in range(len(mot)):
    if mot[i] in lettre:
      res=res+1
  return res