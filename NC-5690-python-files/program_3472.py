def nbOccurrencesLettre(lettre,mot):
  if len(mot)==0:
    return 0
  Cpt=0
  for i in range (len(mot)):
    if mot[i]==lettre:
      Cpt=Cpt+1
  return Cpt
    