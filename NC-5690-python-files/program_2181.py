def nbOccurrencesLettre(lettre,mot):
  if len(mot)==0:
    return None
  else:
    cpt=0
    for elem in mot:
      if lettre==elem:
        cpt=cpt+1
    return cpt

    