def nbOccurrencesLettre(lettre,mot):
  cpt=0
  for c in mot:
    if c==lettre:
      cpt=cpt+1
  return cpt