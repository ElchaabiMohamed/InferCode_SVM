def nbOccurrencesLettre(lettre,mot):
  cpt=0
  for i in range(len(mot)):
    if mot[i]==lettre:
      cpt+=1
  return res