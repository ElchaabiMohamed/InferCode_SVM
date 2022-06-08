def nbOccurrencesLettre(lettre,mot):
  cpt=0
  if len(mot)==0:
    cpt=0
  else:
    for elem in mot:
      if lettre==elem:
        cpt=cpt+1
  return cpt